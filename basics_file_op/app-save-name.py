name = input("enter your name please: ")

# ### Save it to a file
file = open("name.txt", "w")
file.write(name)
file.close()