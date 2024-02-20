from os import system
robo_r = 0
robo_c = 0
option = ''
gmap = [
    ['X',' ',' ',' ',' '], #0
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ']    
#      0   1  2    3  4
]

print(gmap[0][4])

while option != 'x':
    ################ PRINT THE MAP #################
    system ("cls")
    print("-"*12)

    for r in range(5):
        print("|", end = "")
        for c in range (5):
            print(gmap[r][c], end = " ")
        print("|")
    print("-"*12)


    print("\n\nCONTROLS: \na - left\nd-right\nw -up\ns - down\nx-exit")
    ##################################################

    ###############CONTROLS###########################
    option = input (" >> ")
    if option == 'd' and robo_c < len(gmap[robo_c])-1:
        gmap[robo_r][robo_c] = ' ' # remove from current location
        robo_c += 1
        gmap[robo_r][robo_c] = 'x'
        option = input (" >> ")
    elif option == 's' and robo_r < len(gmap[robo_r])-1:
        gmap[robo_r][robo_c] = ' ' # remove from current location
        robo_r += 1
        gmap[robo_r][robo_c] = 'x'
    #HW1: Add movement left, up
    #Add limits    
    elif option == 'w' and robo_r >0:
        gmap[robo_r][robo_c] = ' ' # remove from current location
        robo_r -= 1
        gmap[robo_r][robo_c] = 'x'
    elif option == 'a' and robo_c > 0:
        gmap[robo_r][robo_c] = ' ' # remove from current location
        robo_c -= 1
        gmap[robo_r][robo_c] = 'x'
    elif option == 'x':
        print ('GAME OVER')
    ####################################################
    
