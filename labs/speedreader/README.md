# Python Speedreader

## Timings

20 minutes

## Summary

A simple speedreading program created via scripting. There are only four steps!

## Guide

Step 1 - import libraries:

```
import win32com.client
import time
```

The win32com.client module creates a connection to Notepad App in windows and sends keys to it

Step 2 - Initialise shell connection using win32com.client.Dispatch("WScriptshell"):

```
shell = win32com.client.Dispatch("WScript.Shell")
shell.Run("notepad")
time.sleep(1)
shell.AppActivate("Notepad")
```
The sleep method from time is to make sure Windows isn't sent the data too quickly for it to handle.

Step 3 - Now write a nice message to the user:

```
### Message

msg = """Hello World


sample@*****.com
12:50pm : 10 minutes ago
to me

This is a sample message. Sorry for the pointlessness of it.

From pointless message guy
by The other pointless message guy
"""
```

Step 4 - Finally we need to loop in order to create the time delay and send each character to Notepad:

```
delay=0.04
for i in msg:
    time.sleep(delay)
    shell.SendKeys(i, 0)
```

Full code:

```
import time
import win32com.client

###Shell Connection
shell = win32com.client.Dispatch("WScript.Shell")
shell.Run("notepad")
time.sleep(1)
shell.AppActivate("Notepad")

###Message
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
```

## Watch it work

First make sure you have win32com module. Run `pip install pywin32`

After that just make sure you are in the correct directory and run `python main.py` or whatever you have called your file. It should open a new notepad and type out the message we set in front of your very eyes!