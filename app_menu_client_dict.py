
from os import system
client ={
    "name"              :"John Doe",
    "acc"               :"0123456789012",
    "balance_amount"    : 100000,
    "balance_currency"  : "USD"   
}
#           key            value
client["card_number"] = "1111-2222-3333-4444"
client["card_pin"] ="1234"

run = True
while run:
    system("cls")

    print ('#################### MENU ##################')
    print ("1. Check your account balance")
    print ("2. Change pin code")
    print ("3. Add money to the card")
    print ("4. exit")

    option = int(input("choose > "))

    if option == 1:
        system("cls")
        print(f"Account balance:", client["balance_amount"])
        input ("hit enter to continue ...")

    if option == 2:          
        new_pin_code = input("Please introduce the new pin code: ")
        if new_pin_code != client["card_pin"]:
            client["card_pin"] = new_pin_code
            show_pin = input("Do you want to see the pin on the screen? (yes/no)")
            if show_pin == "yes":
                print("Your new pin is", client["card_pin"])
        input ("hit enter to continue ...")

    if option == 3:
        add_money_check = input("Do you want to add money on the card? (yes/no) ")
        if add_money_check == "yes":
            check_card_number = input("Introduce card number: ")
            if check_card_number == client["card_number"]:
                check_pin = input("Introduce your pin: ")
                if check_pin == client["card_pin"]:
                    added_balance = int(input(" Introduce the amount you want to add on the card : "))
                    client["balance_amount"] += added_balance
                else:
                    print("Wrong pin")
            else:
                print("Wrong card number")
        input ("hit enter to continue ...")
        
    if option == 4:
      print("Have a nice day")
      run = False
         #quit()