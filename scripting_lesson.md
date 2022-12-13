# Python scripting

## Timings

60 minutes

## This lesson includes

* What is scripting?
* Why Python for scripting
* Why scripting is important for DevOps engineers
* Using core modules to automate tasks
* Further labs to automate JSON and YAML tasks

## What is Scripting?

Scripting is simply a piece of code that is used to automate system oriented tasks. When you write code that carries out a practical task without needing compiling, this can be called scripting. Compare this to programming, which refers to the development of software applications.

A key difference between the two concepts is the scope of what they try to achieve. Scripting is typically used for tasks that are specific and limited in their scope. For example automating a particular workflow or performing a set of actions that you know  will be repeated often. Programming in comparison is used for developing more complex and general-purpose software solutions.

Another difference between scripting and programming is the level of abstraction and flexibility they provide. Scripting languages are often designed to be easy to use and understand. They generally allow for rapid development of scripts, but are in return, less powerful and flexible as programming languages. Programming languages tend to be more powerful and provide more control over the details of software being developed.

So remember, scripting is for completing specific, limited tasks while programming is used for development of more complex general purpose software applications. Remember we are DevOps engineers =, not developers! So we want to fins the easiest way for us to carry out our tasks. This is why scripting is ideal for us in many situations.

Scripts are almost always written in 'high-level' langauges such as Python, Bash, Ruby among others.

## Why Python then?

Python is perfect for scripting. We have already been learning it as a programming langauge and the reasons we chose it for that are largely similar as to why we chose it for scripting:

- Easy to understand
- Many libraries
- Large community
- Language interoperability (can talk to other langauges, OS's and software)

## Why is scripting important for DevOps engineers?

As DevOps engineers, we want to make the SDLC as smootha dn effcient as possible. In our quest to do this, there are many different jobs we need to complete. These are often repetitva and mundance. For this reason we look to make it easier for these tasks to be executed when they are going to be done on a regular basis. This can mean automation, but it can also mean taking a long, drawn out process and condensing it down to a single command. And this is what we use scripting for. We can use Python scripts to make reptitive tasks complete by simply executing our script. 

**Here are just some examples of way we use scripts in DevOps:**

1. Python script to query a database
2. Python script to execute a shell command or script
3. Query logs for alerts
4. Python script to take a backup
5. Python script for K8 containers
6. Python script to fetch I.P's of an autoscaling group
7. Lambda function to stop instances on a weekend
8. Python script for ETL jobs
9. Find the expiry date of an SSL certificate
10. Develop CLI applications using Python
11. Automating CRUD
12. Custom scripts for config management

# Let's get scripting!

## Basics of scripting in Python

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


## Summary

You just:

* Learned the difference between scripting and programming
* Why scripting is useful to us as DevOps engineers
* How to write basic scripts, using core Python modules

## Further lessons and labs:

* [os module in depth](https://github.com/LSF970/python_scripting/tree/main/labs/01_os)
* [json module in more depth](https://github.com/LSF970/python_scripting/tree/main/labs/02)json)
* [Scripting to automate yaml](https://github.com/LSF970/python_scripting/tree/main/labs/03_yaml)
* [Automation with boto 3](https://github.com/LSF970/python_scripting/tree/main/labs/04_boto3)
* [speedreader mini-project](https://github.com/LSF970/python_scripting/tree/main/labs/05_speedreader) 
