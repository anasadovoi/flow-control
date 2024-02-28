#LEGEND :
# 0 - free
# 1 - reserved
# 2 - bought
from time import sleep

seats=   [0, 0, 2, 2, 2, 1, 1, 0]
# index = 0, 1, 2, 3 ..........7
option = -1

while option != 0:
    # iterative count algorithm#########
    # HW1: let's say freee_seats = len(seats)
    free_seats = len(seats)
    for pi in range(len(seats)):
        if seats[pi] != 0:
            free_seats -= 1
    # free_seats = 0
    # for pi in range(len(seats)):
    #     if seats[pi] == 0:
    #         free_seats += 1
    #  #################################


    ############## PLOT ##################
    print()
    for pi in range(len(seats)):
            print("",pi+1,"", end = "  ")
    print()
    for pi in range(len(seats)):
        if seats[pi] == 1:
            print("|-|", end = "  ")    
        elif seats[pi] == 2:
            print("|+|", end = "  ")
        else:
            print("| |", end = "  ")
    print("\nFree seats: ", free_seats)
    print("\n")
    ############## PLOT ##################

    # #### show MENU
    print("MENU")
    print("1. Book")
    print("2. Buy")
    print("3. Cancel")
    print("0. Exit")
    print("-------------------------")
    # #####################################



    option = int(input (" >>> "))
    # HW2: Check conditions
    #       - boundaries
    #       - check if the place is free    
    # Add buy and cancel(only booked can be canceled free and bought can't be canceled)
         
    if option == 1:
         place = int(input("which place?"))
         if place<=0 or place > len(seats):
              print("The place you chose doesn't exist")
         elif seats[place - 1] == 0:
              seats[place - 1] = 1
         elif seats[place - 1] != 0:
              print("\nThis seat is not available, choose another one")
              sleep(3)
    if option == 2:
         place = int(input("which place?"))
         if place<=0 or place > len(seats):
              print("The place you chose doesn't exist")
         elif seats[place - 1] == 0:
              seats[place - 1] = 2
         elif seats[place - 1] != 0:
              print("\nThis seat is not available, choose another one")
              sleep(3)
    if option == 3:
         place = int(input("which place?"))
         if place<=0 or place > len(seats):
              print("The place you chose doesn't exist")
         elif seats[place - 1] == 1:
              seats[place - 1] = 0
         elif seats[place - 1] in(0,2):
              print("\nThis seat can not be canceled, choose another one")
              sleep(3)