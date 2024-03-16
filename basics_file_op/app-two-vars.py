
file = open ("data.txt", "r")

data = file.read()

print(f"'{data}'")

names = data.split(" ")
name_1, name_2 =names

print(name_1)
print(name_2)