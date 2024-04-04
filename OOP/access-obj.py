#PRIVATE members
# OOP - Encapsulation
#                   protect the content from inside the capsle from the outside environment
class Box:
    def __init__(self, content) -> None:
        if content != None:
            self.__content = content #_conntent can't be accessed from outside, can be changed from outside #__content - can't be accesed and cheanged from outside the class
        else:
            print("ERROR! None can not be content")    

    def __str__(self):
        return f"BOX[{self.__content}]"
    
#################################################
    
b1 = Box("A good book")
b2 = Box("A Music disc")

b1.__content = None
print(b1)
print(b2)