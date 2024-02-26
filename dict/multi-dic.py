product ={
'name' : 'xPhone X',
'used' : 'True',
'year' : 2020,
'brand': 'Peach',
'price': {
    'value'   : 1000,
    'currency': "EUR"
}
}

# access name and price -> print()
print(product['name'])
print(product['price']['value'],product['price']['currency'] )