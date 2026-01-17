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
# OS Task Manager Simulation

<p align="center">
    <img src="https://img.icons8.com/ios-filled/50/000000/task-manager.png" alt="Task Manager Icon" width="60"/>
</p>

---

## 📋 Part 1: Process Scheduling

### Scenario
| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
|   P1    |      0       |     5      |
|   P2    |      1       |     3      |
|   P3    |      2       |     1      |

### FCFS (First-Come, First-Served)
#### Gantt Chart

<table>
    <tr>
        <td bgcolor="#4CAF50" align="center">P1</td>
        <td bgcolor="#2196F3" align="center">P2</td>
        <td bgcolor="#FFC107" align="center">P3</td>
    </tr>
    <tr>
        <td align="center">0 - 5</td>
        <td align="center">5 - 8</td>
        <td align="center">8 - 9</td>
    </tr>
</table>

#### Waiting Time Calculation
- **P1**: 0 (starts immediately)
- **P2**: 5 - 1 = 4
- **P3**: 8 - 2 = 6
- **Average Waiting Time:** (0 + 4 + 6) / 3 = **3.33**

### Round Robin (Quantum = 2)
#### Gantt Chart

<table>
    <tr>
        <td bgcolor="#4CAF50" align="center">P1</td>
        <td bgcolor="#2196F3" align="center">P2</td>
        <td bgcolor="#4CAF50" align="center">P1</td>
        <td bgcolor="#FFC107" align="center">P3</td>
        <td bgcolor="#2196F3" align="center">P2</td>
        <td bgcolor="#4CAF50" align="center">P1</td>
    </tr>
    <tr>
        <td align="center">0 - 2</td>
        <td align="center">2 - 4</td>
        <td align="center">4 - 6</td>
        <td align="center">6 - 7</td>
        <td align="center">7 - 8</td>
        <td align="center">8 - 9</td>
    </tr>
</table>

#### Waiting Time Calculation
- **P1**: (0) + (4-2) + (8-6) = 0 + 2 + 2 = 4
- **P2**: (2-1) + (7-4) = 1 + 3 = 4
- **P3**: (6-2) = 4
- **Average Waiting Time:** (4 + 4 + 4) / 3 = **4.0**

#### Which is More Responsive?
**Round Robin** is more responsive for interactive systems, as it gives each process a fair share of CPU time, reducing response time for short jobs.

---

## 🔒 Part 2: Process Synchronization

### What Could Go Wrong Without Synchronization?
If both processes increment the counter simultaneously, race conditions can occur, leading to incorrect results (lost updates).

### Synchronization Mechanism: Mutex
Use a mutex to ensure only one process can access the counter at a time.

#### Pseudocode
```pseudo
mutex lock
for i = 1 to 100:
        lock(mutex)
        counter = counter + 1
        unlock(mutex)
```

---

## 🧠 Part 3: Memory Management

### Scenario
- Page reference string: 1, 2, 3, 2, 4, 1, 5
- Frames: 3

### FIFO Page Replacement
| Step | Pages in Frames | Page Fault? |
|------|-----------------|-------------|
|  1   | 1               | Yes         |
|  2   | 1,2             | Yes         |
|  3   | 1,2,3           | Yes         |
|  4   | 1,2,3           | No          |
|  5   | 2,3,4           | Yes         |
|  6   | 3,4,1           | Yes         |
|  7   | 4,1,5           | Yes         |
|      |                 |             |
|      | **Total Faults**| **6**       |

### LRU Page Replacement
| Step | Pages in Frames | Page Fault? |
|------|-----------------|-------------|
|  1   | 1               | Yes         |
|  2   | 1,2             | Yes         |
|  3   | 1,2,3           | Yes         |
|  4   | 1,2,3           | No          |
|  5   | 2,3,4           | Yes         |
|  6   | 3,4,1           | Yes         |
|  7   | 4,1,5           | Yes         |
|      |                 |             |
|      | **Total Faults**| **6**       |

#### Which Performs Better?
In this case, both have the same faults, but LRU generally performs better in practice because it replaces the least recently used page, which is less likely to be needed soon.

---

## 💽 Part 4: Disk Scheduling

### Scenario
- Initial head at 53
- Requests: 98, 183, 37, 122, 14, 124, 65, 67

### FCFS (First-Come, First-Served)
Order: 53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67

| Move         | Distance |
|--------------|----------|
| 53 → 98      |   45     |
| 98 → 183     |   85     |
| 183 → 37     |  146     |
| 37 → 122     |   85     |
| 122 → 14     |  108     |
| 14 → 124     |  110     |
| 124 → 65     |   59     |
| 65 → 67      |    2     |
| **Total**    | **640**  |

### SSTF (Shortest Seek Time First)
Order: 53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183

| Move         | Distance |
|--------------|----------|
| 53 → 65      |   12     |
| 65 → 67      |    2     |
| 67 → 37      |   30     |
| 37 → 14      |   23     |
| 14 → 98      |   84     |
| 98 → 122     |   24     |
| 122 → 124    |    2     |
| 124 → 183    |   59     |
| **Total**    | **236**  |

#### Which is More Efficient?
**SSTF** is more efficient, minimizing total head movement and improving performance.

---

## 👤 Author

**idrissbado**

---

## 🚀 How to Use

1. Review the README for explanations, Gantt charts, and tables.
2. All solutions are provided in a clear, professional format.
3. Already pushed to GitHub: [OSTaskManager](https://github.com/idrissbado/OSTaskManager)
