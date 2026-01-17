# OS Task Manager Simulation

![🖥️](https://img.icons8.com/ios-filled/50/000000/task-manager.png)

## Part 1: Process Scheduling

### Scenario
- **P1**: arrives at time 0, burst = 5
- **P2**: arrives at time 1, burst = 3
- **P3**: arrives at time 2, burst = 1

### FCFS (First-Come, First-Served)
#### Gantt Chart
```
| P1 |    P2   | P3 |
0    5    8    9
```
#### Calculations
- **P1**: Waiting = 0
- **P2**: Waiting = 5 - 1 = 4
- **P3**: Waiting = 8 - 2 = 6
- **Average Waiting Time** = (0 + 4 + 6) / 3 = **3.33**

### Round Robin (Quantum = 2)
#### Gantt Chart
```
| P1 | P2 | P1 | P3 | P2 | P1 |
0    2    4    6    7    8    9
```
#### Calculations
- **P1**: Waiting = (0) + (4-2) + (8-6) = 0 + 2 + 2 = 4
- **P2**: Waiting = (2-1) + (7-4) = 1 + 3 = 4
- **P3**: Waiting = (6-2) = 4
- **Average Waiting Time** = (4 + 4 + 4) / 3 = **4.0**

### Responsiveness
- **Round Robin** is more responsive for interactive tasks because it shares CPU time more fairly, reducing response time for all processes.

---

## Part 2: Process Synchronization

### Problem Without Synchronization
- Both processes may read, increment, and write back the counter simultaneously, causing lost updates (race condition).

### Solution: Mutex
- Use a mutex to ensure only one process increments the counter at a time.

#### Pseudocode
```
mutex lock
for i = 1 to 100:
    lock(mutex)
    counter = counter + 1
    unlock(mutex)
```

---

## Part 3: Memory Management

### Scenario
- Page reference string: 1, 2, 3, 2, 4, 1, 5
- Frames: 3

### FIFO Simulation
- 1, 2, 3 (faults: 3)
- 2 (hit)
- 4 (replace 1, faults: 4)
- 1 (replace 2, faults: 5)
- 5 (replace 3, faults: 6)
- **Total Faults: 6**

### LRU Simulation
- 1, 2, 3 (faults: 3)
- 2 (hit)
- 4 (replace 1, faults: 4)
- 1 (replace 3, faults: 5)
- 5 (replace 2, faults: 6)
- **Total Faults: 6**

### Comparison
- Both have 6 faults here, but LRU usually performs better as it replaces the least recently used page, which is often less likely to be needed soon.

---

## Part 4: Disk Scheduling

### Scenario
- Head at 53
- Requests: 98, 183, 37, 122, 14, 124, 65, 67

### FCFS
- 53→98 (45)
- 98→183 (85)
- 183→37 (146)
- 37→122 (85)
- 122→14 (108)
- 14→124 (110)
- 124→65 (59)
- 65→67 (2)
- **Total: 45+85+146+85+108+110+59+2 = 640**

### SSTF (Shortest Seek Time First)
Order: 53→  65 (12), 67 (2),  37 (30), 14 (23), 98 (84), 122 (24), 124 (2), 183 (59)
- **Total: 12+2+30+23+84+24+2+59 = 236**

### Conclusion
- **SSTF** is more efficient, minimizing total head movement.

---

## Author
- [Your Name]

---

## How to Use
1. Review the README for explanations and Gantt charts.
2. Push to GitHub: 
   ```
   git init
   git remote add origin https://github.com/idrissbado/OSTaskManager.git
   git add .
   git commit -m "Initial commit: OS Task Manager simulation"
   git push -u origin master
   ```
