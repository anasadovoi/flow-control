def printStar():
    print('*', end=' ')


def printStarRow(w):
    for i in range(w):
        printStar()
    print()

def printStarRect(w,h):
    if w>0 and h>0:
     for i in range(h):
        printStarRow(w)
    else:
       print("Dimensions cannot be negative !")


###################
printStarRect(1,7)

# HW1 draw the complete diagram




