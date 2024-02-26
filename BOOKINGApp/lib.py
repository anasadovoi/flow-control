from os import system
option = 0
running = True
destinations =[]
prices =[]

def readDestination():
    global destinations
    file = open("BOOKINGApp\data\destinations.txt", "r")
    lines = file.readlines() # '\n'
    for line in lines:
        destinations.append(line.strip("\n"))

    print(destinations)
    file.close()

def readPrices():
    global prices
    file = open("BOOKINGApp\data\prices.txt", "r")
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
    for i in range(len(destinations)):
        print(f"{destinations[i]:>20}{prices[i]:10}")
    
    input("hit enter ...")

def searchDestination():
    destination = input("enter destination name: ")
    found = destination in destinations
    # "Paris" in["Paris\n", ...""]
    print(found)    
    if found:
        print(f"Destination '{destination}' is available")
        #HW3
        #   * ask for ticket quantity
        #   * calculate total cost
        #   * ask for confirmation
        nr_of_tickets = int(input("How many tickkets do you want? "))
        for i in range(len(destinations)):
            if destination == destinations[i]:
                total_cost= nr_of_tickets * prices[i]
        print("Total cost: ", total_cost)
        decision_to_buy = input("Do you want to buy?(yes/no)")
        if decision_to_buy == "yes":
            print("Thank you for your purchase!")
        else:
            print("We are sad to see you going with no tickets!")
    else:
        print(f"Destination '{destination}' is NOT AVAILABLE")
    input("hit enter ...")
