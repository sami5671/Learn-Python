import json

# Python object to JSON String

personOBJ = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChild": False,
    "titles": ["Engineer", "programmer"]
}

personJSON = json.dumps(personOBJ, indent=4)
print(personJSON)


# JSON String to Python object

personJSON = '{"name": "John", "age": 30, "city": "New York", "hasChild": false, "titles": ["Engineer", "programmer"]}'
personOBJ = json.loads(personJSON)

print(personOBJ["name"])


# python object --->to JSON string  ---->to file write

personOBJ = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChild": False,
    "titles": ["Engineer", "programmer"]
}

with open("person.json", 'w') as personJSONFile:
    json.dump(personOBJ, personJSONFile, indent=4)


# JSON File read --->  python obj ----> to JSON string

with open("person.json", "r") as personOBJFile:
    personOBJ = json.load(personOBJFile)
    personJSON = json.dumps(personOBJ, indent=4)
    print(personJSON)