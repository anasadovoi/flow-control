# CC -custom coding system

#         4 bits
#        |      |
ds = {
    "0": "□□□□",
    "1": "□□□■",
    "2": "□□■□",
    "3": "□□■■",
    "4": "□■□□",
    "5": "□■□■",
    "6": "□■■□",
    "7": "□■■■",
    "8": "■□□□",
    "9": "■□□■",
    "a": "■□■□",
    "b": "■□■■",
    "c": "■■□□",
    "d": "■■□■",
    "e": "■■■□",
    "f": "■■■■"
}

car_info = ["d", "e", "a", "1", "1","2","1", "1"]

from os import system
system("cls")

#############################
for i in range(len(car_info)):
    if i%2 ==0:
        print()
    print(ds[car_info[i]], end="")


print()
print()
    