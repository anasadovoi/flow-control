#draw a square "+" with a given size
from os import system

#HW1 
#   refactor the code so it can draw any rectangle size
system("cls")
size = int(input('size: '))
length = size *size

# + + + + +
# + + + + +
# + + + + +
# + + + + +
# + + + + +

n = 1
print()
while n <= length:
    print("+ ", end="")

    if n % size == 0:
        print()
    
    n +=1

print()