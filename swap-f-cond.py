people = ["Johny", "Marry", "Francis"] # top 3 devs in a company
# index     0          1        2


print("BEFORE",people)
#HW: add code -> user -> placeA , place B to swap
#+check boundaries
placeA = int(input("Choose position 1: "))
placeB = int(input("Choose position 2: "))
if placeA not in range(len(people)) or placeB not in range(len(people)): 
    print("Please try again, you choose an inexistent position")
else:
    temp = people[placeA] #"Johny"
    people[placeA] = people[placeB] # "Marry" -> "Johnny"
    people[placeB] = temp

    print("AFTER",people)