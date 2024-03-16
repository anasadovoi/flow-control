## Utility function



data = [20,30,40]
other_longer_data = [1,2,3,4,5,6,7,8,4]

# -----
# | 20 |
# -----
# | 30 |
# -----
# | 40 |


## DEFINITION
#####################
def printDataTable(data):
    for i in range(len(data)):
        print("------")
        print(f"|{data[i]:^4}|")

    print("-----")


printDataTable(other_longer_data)