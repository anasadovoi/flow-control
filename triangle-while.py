from os import system
# draw this triangle
#HW1: size from keyboard

#      +    
#    + + + 
#  + + + + +

system("cls")

#print ("    +")
#print ("  + + +")
#print ("+ + + + +")

#n = 0
#while n < 3:
#    print("  " *(2-n), "+ " * (2*n+1))
#    n+=1
size = int(input('Insert triangle size: '))
n = 0
while n < size:
    print("  " *(size-n), "+ " * (2*n+1))
    n+=1    