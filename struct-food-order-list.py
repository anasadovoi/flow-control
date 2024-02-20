# order info -> list

order_food_names = ["Pizza", "Salad", "Soup "]
order_food_price = [75.00,     45.00,  15.00]
order_food_q     = [    2,         1,      2]
# index                 0,      1       2
total = 0

for i in range(len(order_food_names)):
    #HW2: calculate total - > print()
    total_line = order_food_price[i] * order_food_q[i]
    total += total_line
    print((i+1), order_food_names[i], order_food_price[i], "x", order_food_q[i], "=", total_line)

print("#####Total########", total)
