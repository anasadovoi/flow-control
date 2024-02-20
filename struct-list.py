#Python Data Structures

days  = ["Mo", "Tu", "Wd", "Th", "Fr", "Sa", "Su" ]
temps = [10.0, 9.0 ,  8.0,   0.0, -5.0, -10.0, 0.0]
#           0,    1,    2,     3,    4,     5,   6

##HW1: rewrite this code with while

#for i in range(7):
#    if temps[i] <= 0:
#        sign = "*"
#    else:
#        sign = " "
#    print(sign, days[i], temps[i])

i=0
while i < 7:
    if temps[i] <= 0:
        sign = "*"
    else:
        sign = " "
    print(sign, days[i], temps[i])
    i +=1

