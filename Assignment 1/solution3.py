import psutil

# Maximum allowed instances for each process
MAX_INSTANCES = 2

# Function to count the instances of a given process name
def count_instances(process_name):
    count = 0
    # Iterate over all running processes
    for proc in psutil.process_iter(['name']):
        # Check if the name of the process matches the given process name
        if proc.info['name'] == process_name:
            count += 1
            if count > MAX_INSTANCES:
                proc.kill()
    return count

# Function to monitor the applications and check the number of instances
def monitor_applications(app_list):
    # Iterate over each application in the list
    for app in app_list:
        # Get the process name of the application
        process_name = app['process_name']
        # Count the running instances of the process
        running_instances = count_instances(process_name)
        # Check if the running instances exceed the maximum allowed instances
        if running_instances > MAX_INSTANCES:
            print(f"Exceeded maximum allowed instances for {process_name}!")
        else:
            # Print the process name and the number of running instances
            print(f"{process_name}: {running_instances}/{MAX_INSTANCES}")

# List of applications to monitor
app_list = [
    {'process_name': 'chrome.exe'},
    {'process_name': 'notepad.exe'},
    {'process_name': 'calc.exe'},
    {'process_name': 'msedge.exe'}
]
monitor_applications(app_list)