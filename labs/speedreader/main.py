#### Import time for sleep method
import time
#### Import win32com.client to access Notepad (Dispatch method)
### Note, run `pip install pywin32`` if module not found
import win32com.client

###Shell Connection
shell = win32com.client.Dispatch("WScript.Shell")
### Run notepad
shell.Run("notepad")
time.sleep(1)
shell.AppActivate("Notepad")

###Message to be written in notepad
msg="""Hello World 


sample@*****.com
12:50pm : 10 minutes ago
to me

This is a sample message. Sorry for the pointlessness of it.

From pointless message guy
by The other pointless message guy
"""  

###For Loop for sending characters in sequence with a delay
delay=0.04
for i in msg:
    time.sleep(delay)
    shell.SendKeys(i, 0)

### End of program, run `python main.py` to see it in action.