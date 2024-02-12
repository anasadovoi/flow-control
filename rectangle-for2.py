# ----------
# |   |    |
# |   |    |
# |--------|
# |   |    |
# |   |    |
# ----------


from os import system
system ("cls")
print()

w = int(input(('width: ')))
h = int(input(('height: ')))

for r in range(h):    # 0..5
    for s in range (w): #0..4
        if r == 0 or  r == h -1:
            print("--", end = "") 
        elif s ==0:
            print("| ", end = "")         
        elif s == w -1:
            print(" |", end = "")
# HW1:
#    add middle v/h lines
        elif s == int(w/2) and r != int(h/2) and (0< r < h-1 ):
           print ("| ", end="")
        elif r == int(h/2) and (0< s < w-1 ) :
           print ("--", end="")
        else:
            print("  ", end = "")
    print()



print()

