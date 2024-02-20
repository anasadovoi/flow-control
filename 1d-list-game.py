from os import system

# HW: if condition ----> move right/left limits
# HW2: add variable  hp =100, each time DANGER hp -50
#it's zero - game over
robo_x = 6 # coord
gmap= [' ', ' ',' ', '⚠',' ', ' ','▣', ' ','⚠', ' '] # LIST, THE MAP 10 VALUES
# index 0    1    2   3   4    5   6    7   8   9
option = ''
over = False
hp = 100

while option != 'x':
    ################ PRINT THE MAP #################
    system ("cls")
    print("-"*20)

    for i in range(len(gmap)):
        print(gmap[i], end =" ")

    print()
    print("-"*20)

    for i in range(len(gmap)):
        print(i, end = " ")
    print("\n\nCONTROLS: a - left, d-right, x-exit")
    ##################################################

    ############### CONTROLS #########################
    if over or hp == 0:
        print("YOU FAILED!!!")
        break
 

    option = input (">> ")
    if option == 'a' and robo_x > 0:
        gmap[robo_x] = ' ' # remove from current location
        robo_x -= 1
        if gmap[robo_x] == '⚠':
            hp -= 50
            gmap[robo_x] = '💣'
            #over = True
        else:
            gmap[robo_x] = '▣' # place x on the new position
    elif option == 'd' and robo_x < len(gmap)-1:
        gmap[robo_x] = ' ' # remove from current location
        robo_x += 1
        if gmap[robo_x] == '⚠':
            hp -= 50
            gmap[robo_x] ='💣'
            #over = True
        else:
            gmap[robo_x] = '▣' # place x on the new position
 
    elif option == 'x':
        print ('GAME OVER')
    ####################################################