import os
import time
import psutil

#!!!!!Move the "script.vbs" to usb!!!!!
urscript = 'script.vbs' 

def get_usb_drives():
    """Returns a set of currently connected USB storage drives."""
    partitions = psutil.disk_partitions()
    usb_drives = {p.device for p in partitions if 'removable' in p.opts}
    return usb_drives

def wait_for_usb_drive():
    """Wait until a new USB flash drive is connected."""
    print("Waiting for USB flash drive to connect...")
    initial_drives = get_usb_drives()
    
    while True:
        time.sleep(1)  # Check every second
        current_drives = get_usb_drives()
        
        new_drives = current_drives - initial_drives
        if new_drives:
            print(f"USB flash drive connected: {list(new_drives)[0]}")
            os.chdir(str(new_drives.pop()))#Change the directory to USB drive
            os.system(urscript)
            #Above line is for running your script which is in USB drive.    
            time.sleep(20)
            print('Done')
            current_drives = initial_drives

wait_for_usb_drive()	
