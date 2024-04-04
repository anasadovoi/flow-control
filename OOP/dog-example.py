## keyword - class: schema, type, template...
#          - function -> factory

###############################################
#1. Step -define

class Dog:
    def __init__(self,     name, breed,year, alive):
            self.name = name
            self.breed = breed
            self.year = year
            self.alive = alive

    def printDog(self):
        print(self.name)
        print(self.breed)
        print(self.year)
        print(self.alive)




#2. Step -use
my_dog  = Dog("Tuzik", "BullDog", 2010, True)
my_dog.printDog()

friends_dog  = Dog("Bobster", "labrador", 2010, False)
my_dog.printDog()



