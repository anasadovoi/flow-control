SCALE  = 10

hX = 5
hY = 4

map = "" 
for y in range(SCALE):
    map += str(y) + ". "
    for x in range(SCALE):

        if x == 0 or x == SCALE - 1 or y == 0 or y == SCALE - 1:
            map += "# "
        elif x == hX and y == hY:
            map += "H "
        #HW1 : Mark dangerous zone:   
        #elif (x in (hX +1, hX, hX-1) and y in(hY-1, hY, hY+1)) or (y == hY and x in (hX-2, hX+2)):
        #    map += "x "
        # HW2 : Mark noise area:
        #elif (x in (hX +1, hX, hX-1) and y in(hY-2,hY-1, hY, hY+1, hY+2)) or (y in( hY, hY-1, hY+1) and x in (hX-2, hX+2)):
        #    map += "~ "
        else:
            map += "  "

    map += "\n"                

print(map)

# Mark the dangerous area:

  # # # # # # # # # # 
  #                 # 
  #     x x x       # 
  #   x x H x x     # 
  #     x x x       # 
  #                 # 
  #                 # 
  #                 # 
  #                 # 
  # # # # # # # # # # 

# nOISE AREA
  # # # # # # # # # # 
  #     ~ ~ ~       # 
  #   ~ ~ ~ ~ ~     # 
  #   ~ ~ H ~ ~     # 
  #   ~ ~ ~ ~ ~     # 
  #     ~ ~ ~       # 
  #                 # 
  #                 # 
  #                 # 
 # # # # # # # # # # 