Set WshShell = WScript.CreateObject("WScript.Shell")

' Open Notepad
WshShell.Run "notepad"
WScript.Sleep 500  ' Wait for Notepad to open

textToType = "HAHA!!! YOU HAVE BEEN HACKED"
For i = 1 To Len(textToType)
    WshShell.SendKeys Mid(textToType, i, 1)
    WScript.Sleep 200  ' 0.2-second delay
Next

WScript.Sleep 200
