#Load structure fom JSON file

from json import loads

#save the data
file = open("person.json", "r")
person = loads(file.read()) 
print(person)
file.close()

print(person["interests"][0])