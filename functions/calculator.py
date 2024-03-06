## app <--- two integers        < ---- user
##     < -- choose operation    < ---- user
##           display result      -----> user

def ii(which):
    print("Enter", which,"integer: ", end ="")
    return int(input()) 
a = ii("first")
b = ii("second")

op = input("Choose operation(* / + - **): ") # op ="+"

res = 0
#HW1: next operations: / - **
## wrong operation

if op =="+":
    res = a + b
elif op =="*":
    res = a * b
elif op =="-":
    res = a - b
elif op =="**":
    res = a ** b
elif op =="/":
    res = a / b
else:
    print("Wrong Operation")


print("Result: ", round(res,2))





