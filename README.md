# Intro to Python Scripting

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

## Important Python Modules for DevOps

* [os (Interacting with the operating system)](https://docs.python.org/3/library/os.html)
* [platform (Access to underlying platform data)](https://docs.python.org/3/library/platform.html)
* [subprocess (Subprocess management)](https://docs.python.org/3/library/subprocess.html)
* [sys (System specific parameters and functions)](https://docs.python.org/3/library/sys.html) 
* [psutil (Process and system utilities)](https://github.com/giampaolo/psutil)
* [re (Regular Expression Operations)](https://docs.python.org/3/library/re.html)
* [scapy (Packet manipulation)](https://github.com/secdev/scapy/)
* [Requests (HTTP library)](https://pypi.org/project/requests/)
* [urllib3 (HTTP client)](https://pypi.org/project/urllib3/)
* [logging (Error logging)](https://pypi.org/project/logging/)
* [getpass (Portable password input)](https://docs.python.org/3/library/getpass.html)
* [boto3 (AWK Software development kit, SDK. Allows interaction with AWS from Python)](https://pypi.org/project/boto3/)
* [paramiko (SSH)](https://www.paramiko.org/)
* [JSON (JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [PyYAML (YAML parser & emitter for Python)](https://pyyaml.org/wiki/PyYAMLDocumentation)
* [pandas (Data science, but useful for automating CSV's)](https://pandas.pydata.org/)
* [smtplib (STMP)](https://docs.python.org/3/library/smtplib.html)

## Use cases for scripting in a DevOps role

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

There are many more, these are just some examples.
