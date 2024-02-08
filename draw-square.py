#draw a square "+" with a given size
from os import system

#HW1 
#   refactor the code so it can draw any rectangle size
system("cls")
s1 = int(input('size1: '))
s2 = int(input('size2: '))
length = s1 *s2

# + + + + +
# + + + + +
# + + + + +

n = 1
print()
while n <= length:
    print("+ ", end="")

    if n % s1 == 0:
        print()
    
    n +=1

print()