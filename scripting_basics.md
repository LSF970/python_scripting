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

First lets use sys to check the version of Python we are using with the sys module:

## sys module

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

## os module

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
```

## subprocess module

The subprocess module is used to create and interact with subprocesses managed by our Python interpretor. For example, we can use subprocess to run another python file:

```
subprocess.run(["python", "hello_world.py"])
```

The output of this is 'hellow world' in the terminal:

```
hello world!
```

Note - Be carefful you don't create an inifinte loop. Run your .py file manually first and automate it when you are happy with it's integration.

## math module

The math module lets us do some more complex mathematical operations than basic Python allows. To showcase this lets use the .pi method:

```
pi = math.pi
pi_string = str(pi)
print("The value of pi is " + pi_string)
```

The output is the value of pi in the terminal:

```
The value of pi is 3.141592653589793
```

## random module

The random module is fairly self explanatory. it allows us to randomise values in a number of ways. 
A simple way to use it is to generate a random number between two limiting values:

```
randnum = random.randrange(1, 10)
print(randnum)
```

This will output a random (whole) number between 1 and 10.

## datetime module

The datetime module is extremely useful and will be relied upon heavily as long as you continue to use Python. It allows us to get the date and time in anumber of ways. A basic way to use it is to simply get the current date and time:

```
whatisthedate = datetime.datetime.now()
print(whatisthedate)
```

Example output:

```
2022-12-12 15:00:15.641668
```

## JSON

JSON is something we will look at in more detail soon. It is essentially a human readable language that is great for transporting data between systems. We will be using it often as DevOps engineers. Here is an example of it in action. We can use it to take a Python object and turn it into JSON automatically:

```
x = {
    "name": "John",
    "age": 30,
    "city": "London"
}

y = json.dumps(x)

print(y)

```

The ouput of this is:

```
{"name": "John", "age": 30, "city": "London"}
```

## Can you see how useful that was?

You are now starting to see the power of scripts and scripting. We can create scripts to make tasks/jobs we know we will need to complete faster. That last example was really simple but effective. With just a few lines of code, I can now convert any Python objects into valid JSON, rather than typing it up myself.

This is why we want to teach you scripting. As DevOps engineers we want to automate as much as we can, in order to make the SDLC as smooth as possible. Scripting is one of the ways we can do this. 

## Further lessons and labs:

* [os module in depth](https://github.com/LSF970/python_scripting/tree/main/labs/01_os)
* [Automation with boto 3](https://github.com/LSF970/python_scripting/tree/main/labs/04_boto3)
* [json module in more depth](https://github.com/LSF970/python_scripting/tree/main/labs/02)json)
* [Scripting to automate yaml](https://github.com/LSF970/python_scripting/tree/main/labs/03_yaml)
* [speedreader mini-project](https://github.com/LSF970/python_scripting/tree/main/labs/05_speedreader) 

