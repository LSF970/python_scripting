# Using Python to check if a JSON file is valid

## Timings

30 Minutes

## Summary

We don't want to try and start parsing a JSON file, only to find out there is something wrong with it. It's a waste of time, and so in manually checking it. So lets make a Python script to check the file quickly. If it is broken we can send it back and ask for a valid copy.

# Code

We read the file and either pass it as a valid JSON file or give an error. We also state whether the error is in the file itself or the program that I am trying to load into.

Run this file with : `python checkjson.py example.json`

```
import os
import sys
import json

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON is valid!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: checkjson.py <file>")
```

If the file is valid, the terminal will print `JSON is valid!`. Now we can check JSON files before we actually work on them!

