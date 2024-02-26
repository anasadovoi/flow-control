# Food Order

order = {
    'client': 'John Doe',
    'item'  : 'salad ',
    'quantity': 9,
    'price' : 55.00
    }
total = order['price'] * order['quantity']
if order['quantity'] > 7:
    order['total'] = total -(total *20/100)
else: 
    order['total'] = total

#####################################
# HW1: modify the co de so -> order['total'] discount 20%
#    when quantity is more than 7 
# HW2: add code so the USER -> input -> 'Do you need delivery?'
#   based on the answer:
#   if total >300 and the user requests delivery
#   add order['delivery'] :  'free'\
#   otherwise if user requests dellivery then:
#   order['delivery'] :  50.00 and 'total' should be updated
print("ORDER for :", order['client'])
print("Food      :", order['item'])
print("Pric x qty:", order['price'],'x',order['quantity'])
print("Total     :", order['total'])

need_del = input('Do you need delivery?(yes/no) ')
if need_del == 'yes' and order['total']>=300.00:
    order['delivery'] = 'free'
elif need_del == 'yes' and order['total']<300.00:
    order['delivery'] = 50.00
    order['total'] += order['delivery']

print(order)
