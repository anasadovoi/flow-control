from os import system
from time import sleep

# ad content

ads = [
    "Buy this Python book for only 0.99$",
    "Try this course of Python for free!!!",
    "Drink a lot of water (2L per day minimum)"
]

ads_duration = [
        
        1.0,
        7.0,
        15.0
]

#Method 1: index only
# index = 0
# while True:
#         system("cls")
#         print(">> ", ads[index])
#         sleep(3)
#         index += 1
#         if index >= len(ads):
#                 index = 0




# Method 2: methods only (python list methods)
# while True:
#         ad = ads.pop(0)
#         system("cls")
#         print(">>", ad, "<<")
#         sleep(3)
#         ads.append(ad)


# HW1: apply the correct duration 
while True:
    ad = ads.pop(0)
    ad_duration = ads_duration.pop(0)
    system("cls")
    print(">>", ad, "<<")
    sleep(ad_duration)
    ads.append(ad)
    ads_duration.append(ad_duration)




