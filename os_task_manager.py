"""
OS Task Manager Simulation
Author: idrissbado
Innovative, visual, and code-driven answers for OS concepts.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# ICONS (Unicode)
ICONS = {
    'cpu': '\U0001F5A5',
    'lock': '\U0001F512',
    'memory': '\U0001F4BE',
    'disk': '\U0001F5B4',
    'author': '\U0001F464',
}

def print_icon(title, icon):
    print(f"{icon}  {title}")

# PART 1: PROCESS SCHEDULING

def fcfs_rr_gantt():
    print_icon("Part 1: Process Scheduling", ICONS['cpu'])
    processes = [
        {'name': 'P1', 'arrival': 0, 'burst': 5},
        {'name': 'P2', 'arrival': 1, 'burst': 3},
        {'name': 'P3', 'arrival': 2, 'burst': 1},
    ]
    # FCFS
    timeline = []
    t = 0
    for p in processes:
        start = max(t, p['arrival'])
        timeline.append((p['name'], start, start + p['burst']))
        t = start + p['burst']
    print("\nFCFS Gantt Chart:")
    for name, start, end in timeline:
        print(f"| {name} ", end='')
    print("|")
    for name, start, end in timeline:
        print(f"{start:2}   ", end='')
    print(f"{timeline[-1][2]}")
    # FCFS Waiting Times
    waits = [timeline[0][1] - processes[0]['arrival']]
    waits.append(timeline[1][1] - processes[1]['arrival'])
    waits.append(timeline[2][1] - processes[2]['arrival'])
    print("FCFS Waiting Times:", waits, "Average:", round(sum(waits)/3,2))
    # RR (quantum=2)
    print("\nRound Robin (q=2) Gantt Chart:")
    rr_timeline = []
    queue = []
    t = 0
    bursts = [5,3,1]
    arrived = [False, False, False]
    done = [False, False, False]
    while not all(done):
        for i, p in enumerate(processes):
            if not arrived[i] and p['arrival'] <= t:
                queue.append(i)
                arrived[i] = True
        if not queue:
            t += 1
            continue
        idx = queue.pop(0)
        p = processes[idx]
        run = min(2, bursts[idx])
        rr_timeline.append((p['name'], t, t+run))
        t += run
        bursts[idx] -= run
        for i, p2 in enumerate(processes):
            if not arrived[i] and p2['arrival'] <= t:
                queue.append(i)
                arrived[i] = True
        if bursts[idx] > 0:
            queue.append(idx)
        else:
            done[idx] = True
    for name, start, end in rr_timeline:
        print(f"| {name} ", end='')
    print("|")
    for name, start, end in rr_timeline:
        print(f"{start:2}   ", end='')
    print(f"{rr_timeline[-1][2]}")
    # RR Waiting Times
    finish = {p['name']:0 for p in processes}
    last = {p['name']:p['arrival'] for p in processes}
    waits = {p['name']:0 for p in processes}
    remaining = {p['name']:p['burst'] for p in processes}
    for name, start, end in rr_timeline:
        waits[name] += start - last[name]
        last[name] = end
        remaining[name] -= (end-start)
        if remaining[name]==0:
            finish[name] = end
    waits_list = [waits['P1'], waits['P2'], waits['P3']]
    print("RR Waiting Times:", waits_list, "Average:", round(sum(waits_list)/3,2))
    # Gantt Chart Plot
    plot_gantt([timeline, rr_timeline], ['FCFS', 'Round Robin'])

def plot_gantt(timelines, labels):
    colors = ['#4CAF50', '#2196F3', '#FFC107']
    fig, axs = plt.subplots(len(timelines), 1, figsize=(8, 2*len(timelines)))
    if len(timelines)==1:
        axs = [axs]
    for ax, timeline, label in zip(axs, timelines, labels):
        for i, (name, start, end) in enumerate(timeline):
            ax.barh(0, end-start, left=start, color=colors[ord(name[-1])-ord('1')], edgecolor='black', height=0.5)
            ax.text((start+end)/2, 0, name, ha='center', va='center', color='black', fontsize=12, fontweight='bold')
        ax.set_yticks([])
        ax.set_title(f"{label} Gantt Chart")
        ax.set_xlim(0, timeline[-1][2]+1)
        ax.set_xlabel('Time')
    plt.tight_layout()
    plt.savefig('gantt_charts.png')
    plt.close()
    print("Gantt charts saved as gantt_charts.png\n")

# PART 2: PROCESS SYNCHRONIZATION

def process_sync_demo():
    print_icon("Part 2: Process Synchronization", ICONS['lock'])
    print("\nWithout synchronization, increments can be lost due to race conditions.\n")
    import threading
    counter = [0]
    def unsafe_inc():
        for _ in range(10000):
            tmp = counter[0]
            tmp += 1
            counter[0] = tmp
    threads = [threading.Thread(target=unsafe_inc) for _ in range(2)]
    for t in threads: t.start()
    for t in threads: t.join()
    print(f"Race condition result (should be 20000): {counter[0]}")
    # Mutex solution
    counter = [0]
    lock = threading.Lock()
    def safe_inc():
        for _ in range(10000):
            with lock:
                counter[0] += 1
    threads = [threading.Thread(target=safe_inc) for _ in range(2)]
    for t in threads: t.start()
    for t in threads: t.join()
    print(f"With mutex: {counter[0]} (correct)\n")

# PART 3: MEMORY MANAGEMENT

def memory_management():
    print_icon("Part 3: Memory Management", ICONS['memory'])
    refs = [1,2,3,2,4,1,5]
    frames = 3
    print("\nFIFO Simulation:")
    fifo_faults = simulate_fifo(refs, frames)
    print("LRU Simulation:")
    lru_faults = simulate_lru(refs, frames)
    print(f"\nFIFO Faults: {fifo_faults}, LRU Faults: {lru_faults}")
    if lru_faults < fifo_faults:
        print("LRU performs better in this case.\n")
    elif lru_faults == fifo_faults:
        print("Both perform equally in this case.\n")
    else:
        print("FIFO performs better in this case.\n")

def simulate_fifo(refs, frames):
    mem = []
    faults = 0
    for r in refs:
        if r not in mem:
            faults += 1
            if len(mem) < frames:
                mem.append(r)
            else:
                mem.pop(0)
                mem.append(r)
            print(f"Page {r}: Fault -> {mem}")
        else:
            print(f"Page {r}: Hit   -> {mem}")
    return faults

def simulate_lru(refs, frames):
    mem = []
    faults = 0
    recent = []
    for r in refs:
        if r not in mem:
            faults += 1
            if len(mem) < frames:
                mem.append(r)
            else:
                # Remove least recently used
                lru = min(recent, key=lambda x: recent.index(x))
                idx = mem.index(lru)
                mem[idx] = r
                recent.remove(lru)
            print(f"Page {r}: Fault -> {mem}")
        else:
            print(f"Page {r}: Hit   -> {mem}")
            recent.remove(r)
        recent.append(r)
    return faults

# PART 4: DISK SCHEDULING

def disk_scheduling():
    print_icon("Part 4: Disk Scheduling", ICONS['disk'])
    head = 53
    reqs = [98, 183, 37, 122, 14, 124, 65, 67]
    print("\nFCFS:")
    fcfs_moves = simulate_fcfs(head, reqs)
    print("SSTF:")
    sstf_moves = simulate_sstf(head, reqs)
    print(f"\nTotal head movement - FCFS: {fcfs_moves}, SSTF: {sstf_moves}")
    if sstf_moves < fcfs_moves:
        print("SSTF is more efficient.\n")
    else:
        print("FCFS is more efficient in this case.\n")

def simulate_fcfs(head, reqs):
    total = 0
    pos = head
    for r in reqs:
        total += abs(pos - r)
        print(f"{pos} -> {r} (move {abs(pos-r)})")
        pos = r
    return total

def simulate_sstf(head, reqs):
    total = 0
    pos = head
    pending = reqs[:]
    while pending:
        next_r = min(pending, key=lambda x: abs(pos-x))
        total += abs(pos-next_r)
        print(f"{pos} -> {next_r} (move {abs(pos-next_r)})")
        pos = next_r
        pending.remove(next_r)
    return total

if __name__ == "__main__":
    print("\n==============================")
    print_icon("OS Task Manager Simulation", ICONS['cpu'])
    print("==============================\n")
    fcfs_rr_gantt()
    process_sync_demo()
    memory_management()
    disk_scheduling()
    print_icon("Author: idrissbado", ICONS['author'])
    print("\nAll results, Gantt charts, and calculations are generated by code. See 'gantt_charts.png' for visual Gantt charts.\n")
