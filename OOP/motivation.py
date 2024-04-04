#Real world structure (dog) ---> code

#2. actions

#2. Actions
def dog_bark():
    print("Whoooof Whoooof!")
def dog_eat(food_kg):
    if(food_kg >= 1):
        print("Whoooof")
    else:
        print("RRRRRRRRRRRRRRRRRRRrrr!!!")


#1. properties

dog= {
    "name": "Tuzic",
    "year" : 2010,
    "breed" : "BullDog",
    "alive" : True,
    "eat" : dog_eat,
    "bark" : dog_bark
}


print(dog["name"])
if dog["alive"]:
    print("Yeeeey!!!")

dog["bark"]()
dog["eat"](0.1)

dog_eat(1)