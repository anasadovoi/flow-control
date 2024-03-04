import os
from os import system
from os.path import exists
from pathlib import Path
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
    print("3. Show existing order")
    print("4. Cancel Order")
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
        nr_of_tickets = int(input("How many tickets do you want? "))
        idx = destinations.index(destination)
        total_cost = prices[idx] *nr_of_tickets
        #for i in range(len(destinations)):
        #   if destination == destinations[i]:
        #        total_cost= nr_of_tickets * prices[i]
        print(f"'{destination}' x {nr_of_tickets} ={total_cost}")
        confirm = input("enter y to confirm:  ")
        if confirm == "y":
            pnc = input("enter your personal number: ")

            file = open(f"BOOKINGApp\data\{pnc}.txt", "w")
            file.write(f"{destination}\n")
            file.write(f"{nr_of_tickets}\n")
            file.write(f"{total_cost}\n")

            print("Order saved")

        else:
            print("We are sad to see you going with no tickets!")
    else:
        print(f"Destination '{destination}' is NOT AVAILABLE")
    input("hit enter ...")


def renderOrder():
    pnc = input("enter your personal number: ")
    if exists(f"{pnc}.txt"):
        file = open(f"{pnc}.txt", "r")
        lines = file.readlines()
        print("Your order details: ")
        for line in lines:
            print(line)
        file.close()
    else: 
        print("Your order does not exist")

    input("hit enter ...")


def deleteOrder():
    pnc = input("enter your personal number: ")
    if exists(f"BOOKINGApp\data\{pnc}.txt"):
        os.remove(f"BOOKINGApp\data\{pnc}.txt")
        print(f'Order {pnc} was successfully deleted')
    else: 
        print("The order you are trying to delete does not exist")

    input("hit enter ...")
