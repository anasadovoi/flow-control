value = 12
# determines if the value is positive or negative
print("Positive") if value >= 0 else print("Negative")

#HW: Add another condition to print "Positive and Odd" every time value is odd and >0, and print "The rest" for the other values
print("Positive and odd") if value % 2 != 0 and value >= 0 else print("The rest")

