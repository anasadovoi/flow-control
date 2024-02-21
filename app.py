#Python /  data structures / dict

client_name             = "John Doe"
client_acc              = "0123456789012"
client_balance_amount   = 100000 #1000.00
client_balance_currency = "USD"

# + -----------dict structure
client ={
    "name"              :"John Doe",
    "acc"               :"0123456789012",
    "balance_amount"    : 100000,
    "balance_currency"  : "USD"   
}
#           key            value

print(client["name"])
print(client["acc"])

client_balance_amount +=1000

print(client["balance_amount"])
client["card_number"] = "1111-2222-3333-4444"
client["card_pin"] = "1234"
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


print(client)

# HW1: based on the data structure above
#       continue this app:
#        - to allow the user to put some money on his account
#        - for comodity the client will enter the money the usual way
#        -  for this the app should ask for card number
#        - also the app should ask the pin code
#        - update the amount in the account

#HW2: add interactivity:
# -menu 1. to check balance, 2. change pin, 3. 

