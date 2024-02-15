import psutil
import csv

# Function to retrieve information about running processes
def run_proc():
    processes = []
    # Iterate over all running processes
    for proc in psutil.process_iter():
        # Get process information such as process ID and name
        process_info = proc.as_dict(attrs=['pid', 'name'])
        # Append process information to the list
        processes.append(process_info)
    return processes

# Function to count the occurrences of each process
def count_processes(processes):
    process_count = {}
    # Iterate over each process
    for process in processes:
        # Extract the process name
        process_name = process['name']
        # Update the count for the process name
        process_count[process_name] = process_count.get(process_name, 0) + 1
    return process_count

# Function to save process information to a CSV file
def save_to_csv(process_count):
    with open('processes.csv', 'w', newline='') as csvfile:
        # Define field names for the CSV file
        fieldnames = ['Process Name', 'Count']
        # Create a CSV writer object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write the header row in the CSV file
        writer.writeheader()
        # Iterate over each process and its count
        for process_name, count in process_count.items():
            # Write the process name and count to the CSV file
            writer.writerow({'Process Name': process_name, 'Count': count})
    # Print a message indicating that process information has been saved
    print("Process information saved to 'processes.csv'")

# Retrieve information about running processes
running_processes = run_proc()

# Count occurrences of each process
process_count = count_processes(running_processes)

# Print process names and their counts
for process_name, count in process_count.items():
    print(f"{process_name}: {count}")

# Save process information to a CSV file
save_to_csv(process_count)