# Round Robin Scheduling
def round_robin(processes, time_quantum):
    remaining_time = [burst_time for _, burst_time in processes]
    current_time = 0
    waiting_time = [0] * len(processes)

    print("Round Robin (Preemptive) Scheduling:")
    
    while True:
        done = True

        for i in range(len(processes)):
            if remaining_time[i] > 0:
                done = False  # There are still processes to execute

                if remaining_time[i] > time_quantum:
                    current_time += time_quantum
                    remaining_time[i] -= time_quantum
                else:
                    current_time += remaining_time[i]
                    waiting_time[i] = current_time - processes[i][1]
                    remaining_time[i] = 0

        if done:
            break  # All processes are complete

    avg_waiting_time = sum(waiting_time) / len(processes)
    print(f"Average Waiting Time: {avg_waiting_time}")


# Sample processes (name, burst_time)
processes = [("P1", 10), ("P2", 5), ("P3", 8)]
time_quantum = 4
round_robin(processes, time_quantum)
