def fcfs_scheduling(processes, burst_times):
    n = len(processes)
    
    # Initialize waiting times and turnaround times
    waiting_times = [0] * n
    turnaround_times = [0] * n
    
    # Calculate waiting time for each process
    waiting_times[0] = 0  # First process has 0 waiting time
    for i in range(1, n):
        waiting_times[i] = waiting_times[i-1] + burst_times[i-1]
    
    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_times[i] = waiting_times[i] + burst_times[i]
    
    # Calculate averages
    avg_waiting_time = sum(waiting_times) / n
    avg_turnaround_time = sum(turnaround_times) / n
    
    return waiting_times, avg_waiting_time, turnaround_times, avg_turnaround_time

def display_schedule(processes, burst_times, waiting_times, turnaround_times):

    print("\n" + "="*60)
    print(f"{'Process':<10}{'Burst Time':<15}{'Waiting Time':<15}{'Turnaround Time':<20}")
    print("-"*60)
    
    for i in range(len(processes)):
        print(f"{processes[i]:<10}{burst_times[i]:<15}{waiting_times[i]:<15}{turnaround_times[i]:<20}")
    
    print("="*60)

def display_gantt_chart(processes, burst_times):

    print("\nGantt Chart:")
    print("-" * 50)
    
    current_time = 0
    chart = "|"
    timeline = "0"
    
    for i in range(len(processes)):
        # Add process to chart
        process_display = f" {processes[i]} ".center(burst_times[i] * 2, "-")
        chart += process_display + "|"
        
        # Update current time
        current_time += burst_times[i]
        
        # Add time marker
        spaces = " " * (len(process_display) - len(str(current_time)) + 1)
        timeline += spaces + str(current_time)
    
    print(chart)
    print(timeline)
    print("-" * 50)

def main():
    while True:
        try:
            # Get number of processes
            n = int(input("Enter the number of processes: "))
            if n <= 0:
                print("Number of processes must be positive. Please try again.")
                continue
            
            processes = []
            burst_times = []
            
            # Get process details
            print("\nEnter process details:")
            for i in range(n):
                process_id = f"P{i+1}"
                processes.append(process_id)
                
                while True:
                    try:
                        burst = int(input(f"Enter burst time for process {process_id}: "))
                        if burst <= 0:
                            print("Burst time must be positive. Please try again.")
                            continue
                        burst_times.append(burst)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")
            
            # Run FCFS scheduling algorithm
            waiting_times, avg_waiting_time, turnaround_times, avg_turnaround_time = fcfs_scheduling(processes, burst_times)
            
            # Display results
            display_schedule(processes, burst_times, waiting_times, turnaround_times)
            display_gantt_chart(processes, burst_times)
            
            print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
            print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
            
            # Ask if user wants to continue
            choice = input("\nDo you want to run another simulation? (y/n): ").lower()
            if choice != 'y':
                print("Thank you for using the FCFS CPU Scheduler. Goodbye!")
                break
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break

if __name__ == "__main__":
    print("\nFirst Come First Served (FCFS) CPU Scheduling Simulator")
    print("------------------------------------------------------")
    main()