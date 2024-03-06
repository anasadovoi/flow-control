## need a function

## "Hello" -- > [ Hello ]
## "Bye" -- > [ Bye ]

## FUNCTION DEFINITION

# def printFormatted(word):
#     print(f'[ {word} ]')
def printFormatted( message ):
    print ("--------------")
    print("[", message ,"]")
    print ("--------------")

## CALL THE FUNCTION
printFormatted("Hello")
printFormatted("Bye")
