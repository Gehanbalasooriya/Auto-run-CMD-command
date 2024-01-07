import wmi
import subprocess

def run_cmd_command(command):
    # Execute the CMD command
    subprocess.call(command, shell=True)

def monitor_usb_device():
    c = wmi.WMI()
    watcher = c.Win32_DeviceChangeEvent.watch_for(
        EventType=2  # Device arrival event
    )

    for event in watcher:
        if 'USBSTOR' in event.DeviceID:
            # You can add additional conditions to filter specific pen drives if needed
            run_cmd_command('your_command_here')

if __name__ == '__main__':
    monitor_usb_device()
