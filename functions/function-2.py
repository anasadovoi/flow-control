#   * generate random 2d array
#   * print 2d array
#   * calculate average value of a 2d array

from random import randint

# SRP
 
#################################
def random2dArray(rows,cols, range_from, range_to):
    matrix=[]

    for ri in range(rows):
        row=[]
        for ci in range(cols):
            row.append(randint(range_from,range_to))

        matrix.append(row)
    return matrix
###################################

###################################
# HW2: add a header
#       size: 5x3
def print2dArray(matrix):
    print(f"Size:{len(matrix):^3}x{len(matrix[0]):^3}")
    for ri in range(len(matrix)):
        for ci in range(len(matrix[0])):
            print(f"{matrix[ri][ci]:5}", end ="")

        print()   

###################################
        
###################################
def average2dArray(matrix):
    s = 0
    h = len(matrix)
    w = len(matrix[0])
    for ri in range(len(matrix)):
        for ci in range(len(matrix[0])):
            s+= matrix[ri][ci]

    average = s / (h*w)
    return average

###################################
data = random2dArray(10,10, 0,10)
print2dArray(data)
a = average2dArray(data)
print(a)
#print(data)