#WHILE - print integers asc
from os import system


start_n = int(input("Introduce the first number: "))
end_n   = int(input("Introduce the last number: "))

if start_n < end_n:
    while start_n <= end_n:
        print(start_n)
        start_n += 1
elif end_n < start_n:
    while end_n <= start_n:
        print(start_n)
        start_n -= 1
else:
    system("cls")
    print("Try again")



#HW
#Add two variables start_n and end_n
# If start_n > end_n order desc
# Use if/else to solve