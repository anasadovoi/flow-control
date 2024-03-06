# create functions that corresponds to * / + -

# pure functions
def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def add(a,b):
    return a/b

def sub(a,b):
    return a/b

# HW1 finish add(), sub()
# HW2: rewrite r = 1+2*3/4

r =add(1, div(mul(2,3),4))
print(r)