# Usb_Autorun

This is a project to run a script when a usb is connected(Like Rubber Ducky)<br>
### !! EDUCATIONAL PURPOSE !!

# Difference b/w usb Rubber Ducky and Autorun

Usb Rubber Ducky has a inbuilt microcontroller which automatically runs the code when usb is connected, But you need to have this code running in ur system and a `script.vbs` in your usb drive.

# Directions for Proper Execution

~ First clone the repo `git clone https://github.com/Romyo-jit/Usb_Autorun.git`<br>
~ CD into Usb_Autorun `cd Usb_Autorun`<br>

#### !!!! Remember you need to move the `script.vbs` to usb<br>

~ Run the Script `python3 usb_autorun.py`<br>
-----Now when u plug the usb drive it should run the script :)------

# script.vbs
In the `script.vbs` there is instruction to open `notepad.exe` and type `HAHA!!! YOU HAVE BEEN HACKED' in ur notepad. You can change the code however u like

# Making executable
You can make a python executable with `pyinstaller`
