import os

def check_process_status(pid):
    if not pid_exists(pid):
        print("Process with PID {} does not exist.".format(pid))
        return

    try:
        # Check process status by sending signal 0
        os.kill(pid, 0)
        print("Process with PID {} is running.".format(pid))
    except OSError:
        print("Process with PID {} is not running.".format(pid))

def pid_exists(pid):
    return os.path.exists('/proc/{}'.format(pid))

# Usage: Call the function with the desired PID
check_process_status(1234)
