item = ["Peter", "Marry"] # this is what we search for
found = [False, False]
container = ["John", "Marry", "Bob"] # this is WHERE we look for
for j in range(len(item)): 
    for i in range(len(container)):
        found[j]    = container[i] == item[j] # boolean
        if found[j]:
            break


#################
print(item)
print(found)

for j in range(len(item)):
    if found[j]:
        print(item[j], "FOUND!")
    else:
        print(item[j], "not FOUND!")

