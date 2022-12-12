# Basics of scripting in Python

Scripts are top-level files, intended for execution by the user (us). Modules can be imported and can EXTEND the power of the scripts you write.

## Python modules

The core of scripting is using modules. Modules allow us to import already created libraries of functions/methods to use without need to do any programming. This allows us to leverage the power of scripts.

The seven core Python modules are:

* Sys
* Os
* Subprocess
* Math
* Random
* DateTime
* JSON

First lets use sys to check the version of Python we are using:

Create a file called sysmodule

Now lets import the module:

```
import sys
```

As sys is a core module, it is installed when we installed Python. Non-core modules will need to be downloaded first using pip.

Now lets use sys to do something:

```
print(sys.version)
```
What does this line of code do? And how does it work even though we didn't define `version`?

Well lets run the file to find out. In terminal run `python sysmodule.py`

The output should be something like:

```
3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)]
```

So by using the sys module we can use built in functions to streamline what we want to do. This is scripting.

## OS Module

Used to interact with the host operating system, mainly around file and folder manipulation.

Import module:

```
import os
```

We can get the current working directory (cwd) using the os module:

```
print(os.getcwd())
```

We can change the cwd with:

```
os.chdir("path")
```

Or make a new directory with:

```
os.mkdir("path")

## Subprocess

Content here

## Math

Content here

## Random

Content here

## DateTime

Content here

## JSON

Content here