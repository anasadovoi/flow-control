#small_ship = int(input("Introduce ship coordinate:  "))
big_ship = int(input("Introduce big ship coordinate:  "))

for x in range(1,11):
    if x == big_ship-1 or x == big_ship or x == big_ship+1:
      print( "W", end="" )
    else:
        print( "~", end="" )
    
    