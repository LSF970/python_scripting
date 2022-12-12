# Using Python to check if a YAML file is valid

## Timings

15 Minutes

## Summary

Assuming you have comlpleted the lab on validating JSON files, we should move on to doing the same for YAML. YAML is used by a number of DevOps tools such as K8, Docker and Ansible. It is extremely syntax sensitive so it is super easy for a YAML file to be invalid. Let's make a script so we can check before we put any time into it.

## Code

You may need to run `pip install pyyaml` in order to import the yaml module. The code is largely the same as the JSON file.

Run this file with : `python checkyaml.py example.yaml`

```
import os
import sys
import yaml

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        yaml.safe_load(file.read())
        file.close()
        print("Validate YAML!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: checkyaml.py <file>")
```
