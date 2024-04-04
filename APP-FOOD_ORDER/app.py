from json import loads
from restaurant import *
# contains order data
order = {

    "items" : []
}


##############################################################

food = loadFood()
while True:
    option = printMenu()

    if option == 0:
        break
    if option == 1:
        printFood(food)
        input("Hit ENTER to continue")

    if option == 2:
        selected_i = int(input("which item:  ")) - 1
        print(f"You've selected <<{food[selected_i]['name']}>>")
        quantity = int(input("How many:  "))
        # HW if+else: check availability
        if quantity <= food[selected_i]['avail'] and quantity > 0:
            price_per_item = quantity * food[selected_i]['price']['amount']
            print(f"<<{food[selected_i]['name']}>> x {quantity} = {price_per_item:8.2f}{food[selected_i]['price']['currency']}")
        elif quantity > food[selected_i]['avail']:
            answer= input(f"Max quantity available is: {food[selected_i]['avail']} do you want to buy this quantity? ")
            if answer == "yes":
                quantity = food[selected_i]['avail']
                price_per_item = quantity * food[selected_i]['price']['amount']
                print(f"<<{food[selected_i]['name']}>> x {quantity} = {price_per_item:8.2f}{food[selected_i]['price']['currency']}")
            else:
             pass
            
        #HW2 ask for confirmation
        #HW3 add -> order["items"] (.append())
        #{
        # "name" : "Soup, "quantity": 10, "total" : {"amount"}
        #    }
           
        input("Hit ENTER to continue")
        
