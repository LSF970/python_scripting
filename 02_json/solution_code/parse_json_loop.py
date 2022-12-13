import json
import os

script_dir = os.path.dirname(__file__)
print("The Script is located at:" + script_dir )
script_absolute_path = os.path.join(script_dir, 'example.json')
print("The Script Path is:" + script_absolute_path)


json = json.loads(open(script_absolute_path).read())
value = json['name']
print(value)

# print the keys and values
for key in json:
    value = json[key]
    print("The key and value are ({}) = ({})".format(key, value))