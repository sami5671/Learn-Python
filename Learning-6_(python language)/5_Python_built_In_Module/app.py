import math
import os
import sys
import datetime
import random
import time
import json

result = math.sqrt(16)
print(result)

directory = os.getcwd()
print(directory)

pythonVersion = sys.version
print(pythonVersion)

currentDateTime = datetime.datetime.now()
print(currentDateTime)

# `generateRandom = random.randint(1,10)` is generating a random integer between 1 and 10 (inclusive)
# using the `randint()` function from the `random` module in Python. The `randint()` function takes
# two arguments, which represent the range within which the random integer should be generated. In
# this case, it will generate a random integer between 1 and 10 and assign it to the variable
# `generateRandom`.
generateRandom = random.randint(1,10)
print(generateRandom)

getTime  = time.time()
print(getTime)

data = '{"name":"Jhon"}'
# `jsonData = json.loads(data)` is converting a JSON formatted string `data` into a Python dictionary
# object `jsonData`. The `json.loads()` function is used to parse a JSON string and convert it into a
# Python object. In this case, it is converting the JSON string `data` which contains a key-value pair
# into a Python dictionary object.
jsonData = json.loads(data)
print(jsonData["name"])
