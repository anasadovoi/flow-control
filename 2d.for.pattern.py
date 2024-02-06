# PATTERN 10x10

# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *

#for i in range (1,101):
#    print("*", end = " ")
#   if i%10 == 0:
#        print()
rx = 5
ry = 5
print()
for y in range (1,11):
    for x in range (1,11):
      if x == rx and y == ry:
        print("R", end = " " )
      elif x ==rx and y == ry - 1:
         print("+", end = " ")
      elif x ==rx and y == ry + 1:
         print("+", end = " ")
      elif y ==ry and x == rx - 1:
         print("+", end = " ")
      elif y ==ry and x == rx + 1:
         print("+", end = " ")
      #HW diagonals   
      elif y ==ry - 1 and x == rx + 1:
         print("+", end = " ")
      elif y ==ry - 1 and x == rx - 1:
         print("+", end = " ")
      elif y ==ry + 1 and x == rx - 1:
         print("+", end = " ")
      elif y ==ry + 1 and x == rx + 1:
         print("+", end = " ")
      else:
         print(".", end = " ")
   
    print()  

print()