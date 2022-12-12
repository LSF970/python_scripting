import sys
import os
import subprocess
import math
import random
import datetime
import json


# Gets version of Python using sys module
print(sys.version)

# Gets cwd using os module
print(os.getcwd())

# Uses subprocess module to run another python file
subprocess.run(["python", "hello_world.py"])

# Get the value of pi with the math module
pi = math.pi
pi_string = str(pi)
print("The value of pi is " + pi_string)

# The random module is both one of the most useful and fun around!
# Here we use it to generate random numbers within a range.
randnum = random.randrange(1, 10)
print(randnum)

# Using DateTime to get the current date and time (it can be used for much more than this!)
whatisthedate = datetime.datetime.now()
print(whatisthedate)

# Using json module to conver a Python objecct to a JSON string
x = {
    "name": "John",
    "age": 30,
    "city": "London"
}

y = json.dumps(x)

print(y)
