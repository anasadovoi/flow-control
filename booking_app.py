from os import system

option = 0
running = True
destinations =[]
prices =[]

def readDestination():
    global destinations
    file = open("destinations.txt", "r")
    lines = file.readlines() # '\n'
    for line in lines:
        destinations.append(line.strip("\n"))

    print(destinations)
    file.close()

def readPrices():
    global prices
    file = open("prices.txt", "r")
    lines = file.readlines() # '\n'
    for line in lines:
        prices.append(float(line))
    print(prices)

def renderMenu():
    global option
    system("cls")
    print("OPTIONS")
    print("1. Search destination")
    print("2. Show destination")
    print("3. ")
    print("0. Exit")
    option = int(input("choose>>>"))

def renderDestinations():
    for destination in destinations:
        print(destination)
    
    input("hit enter ...")

def searchDestination():
    destination = input("enter destination name: ")
    found = destination in destinations
    # "Paris" in["Paris\n", ...""]
    print(found)    
    if found:
        print(f"Destination '{destination}' is available")
    else:
        print(f"Destination '{destination}' is NOT AVAILABLE")
    input("hit enter ...")


################## HOC ###############################
readDestination()
readPrices() 
while running:
    renderMenu()
    if option == 1:
        searchDestination()
    if option == 2:
        renderDestinations()
    if option == 0:
        running = False




