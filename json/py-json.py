#SAVE structure to JSON file
from json import dumps

#data structure

person = {
    "name" : "John",
    "age"  : 30,
    "alive" : True,
    "interests" : [
        "programming",
        "hacking"
    ]
}

#save the data
file=open("person.json", "w")
file.write(dumps(person))
file.close