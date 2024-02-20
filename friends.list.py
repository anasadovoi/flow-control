# FACT:  list of friends

# empty list
friends = []

while len(friends)<100:
    name = input("Add friend name:  ")
    if name == "":
        break
    #HW1: check if the name is already in the list
    if name not in (friends):
        friends.append(name)

print("You have", len(friends), "friends")
for i in range (len(friends)):
    print("    ",i, ">>",friends[i])
