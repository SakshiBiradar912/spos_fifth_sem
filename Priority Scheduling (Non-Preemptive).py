# Priority Scheduling (Non-Preemptive)
def priority_scheduling(processes):
    # Sort by priority (the lower the number, the higher the priority)
    processes.sort(key=lambda x: x[1])

    total_waiting_time = 0
    total_turnaround_time = 0
    waiting_time = 0

    print("Priority (Non-Preemptive) Scheduling:")
    
    for i in range(len(processes)):
        process_name, priority, burst_time = processes[i]

        if i == 0:
            waiting_time = 0
        else:
            waiting_time += processes[i - 1][2]  # Add previous process's burst time

        turnaround_time = waiting_time + burst_time

        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        print(f"Process {process_name}: Waiting Time = {waiting_time}, Turnaround Time = {turnaround_time}")

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")


# Sample processes (name, priority, burst_time)
processes = [("P1", 1, 10), ("P2", 3, 5), ("P3", 2, 8)]
priority_scheduling(processes)
