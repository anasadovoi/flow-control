# from data import name, skills, printData

# print("from app", name, skills)
# printData()

# name = "Mary"
# skills.clear()
# skills.append("design")

# print("After")
# print("from app", name, skills)
# printData()

import data

print("from app", data.name)
data.printData()

data.name = "Mary"

print("After")
print("from app", data.name)
data.printData()