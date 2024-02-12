# flow-control
from os import system

fill = 80


system("cls")
for n in range (5): # 0 .. 4
    if int((100 - fill) / 20) == n:
     print ("+-----+"+"   < ", fill,"%")
    print("|     |")

print("+-----+") 