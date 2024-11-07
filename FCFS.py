def fcfs(processes):
    total_waiting = 0
    total_turnaround = 0
    waiting_time = 0

    for i in range(len(processes)):
        process_name,burst_time = processes[i]

        if i == 0:
            waiting_time = 0
        else:
            waiting_time += processes[i-1][1]
        turnaround_time = waiting_time + burst_time

        total_waiting += waiting_time
        total_turnaround += turnaround_time

        print(f"Process {process_name}: Waiting Time = {waiting_time}, Turnaround Time = {turnaround_time}")

    avg_waiting_time = total_waiting/len(processes)
    avg_turnaround_time = total_turnaround/len(processes)

    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

processes = [('p1',10),('p2',5),('p3',5)]
fcfs(processes)