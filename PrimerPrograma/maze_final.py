import os
import readchar
import random

POS_X = 0
POS_Y = 1

MY_POSITION = [3,2]
NUMBER_OF_OBJECTS = 11
TAIL_LEN = 0
TAIL = []
MAP_OBJECTS = []
END_GAME = False
OBSTACLES_DEFINITION = """\
##   ###################################
 #       ################               
 ##            ##########    ######  ###
 #######        #########    ####    ###
 ###########       ######    ####    ###
  ##########                  ###    ###
   #####################    #####    ###
#    ####################   #####    ###
###       #######           #####    ###
########             #########       ###
#####       ################         ###
########           #########         ###
#################      #################
    ################                    
#           ############################\
"""

#Create map obstacles
OBSTACLES_DEFINITION = [list(row) for row in OBSTACLES_DEFINITION.split("\n")]
MAP_WIDTH = len(OBSTACLES_DEFINITION[0])
MAP_HEIGHT = len(OBSTACLES_DEFINITION)



#Main Loop
while END_GAME == False:
    if MY_POSITION in TAIL:
        print("YOU LOSE!")
        input("Pulsa enter para finalizar...")
        exit()
    # DrawMap
    # Generate random objects in map
    while len(MAP_OBJECTS) < NUMBER_OF_OBJECTS:
        NEW_POSITION = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

        if NEW_POSITION not in MAP_OBJECTS and NEW_POSITION != MY_POSITION and \
                OBSTACLES_DEFINITION[NEW_POSITION[POS_Y]][NEW_POSITION[POS_X]] != "#":
            MAP_OBJECTS.append(NEW_POSITION)
    print("+" + "-" * (MAP_WIDTH * 2) + "-" + "+")
    for CORDINATE_Y in range(MAP_HEIGHT):
        print("|", end=" ")

        for CORDINATE_X in range(MAP_WIDTH):

            CHAR_TO_DRAW = "  "
            OBJECT_IN_CELL = None

            for MAP_OBJECT in MAP_OBJECTS:
                if MAP_OBJECT[POS_X] == CORDINATE_X and MAP_OBJECT[POS_Y] == CORDINATE_Y:
                    CHAR_TO_DRAW = " *"
                    OBJECT_IN_CELL = MAP_OBJECT
            for TAIL_PIECE in TAIL:
                if TAIL_PIECE[POS_X] == CORDINATE_X and TAIL_PIECE[POS_Y] == CORDINATE_Y:
                    CHAR_TO_DRAW = " @"
            if MY_POSITION[POS_X] == CORDINATE_X and MY_POSITION[POS_Y] == CORDINATE_Y:
                CHAR_TO_DRAW = " @"
                if OBJECT_IN_CELL:
                    MAP_OBJECTS.remove(OBJECT_IN_CELL)
                    TAIL_LEN += 1
                    NEW_OBJECT = None
            if OBSTACLES_DEFINITION[CORDINATE_Y][CORDINATE_X] == "#":
                CHAR_TO_DRAW  = " #"

            print("{}".format(CHAR_TO_DRAW), end="")
        print("|")
    print("+" + "-" * (MAP_WIDTH * 2) + "-" + "+")
    # Ask user where he wants to move
    #direction = input("¿Donde te quieres mover? WASD: ")
    direction = readchar.readchar().decode()
    NEW_POSITION = None

    if direction == "w":
        NEW_POSITION = [MY_POSITION[POS_X], (MY_POSITION[POS_Y] - 1) % MAP_WIDTH]
    elif direction == "s":
        NEW_POSITION = [MY_POSITION[POS_X], (MY_POSITION[POS_Y] + 1) % MAP_WIDTH]
    elif direction == "a":
        NEW_POSITION = [(MY_POSITION[POS_X] - 1) % MAP_WIDTH, MY_POSITION[POS_Y]]
    elif direction == "d":
        NEW_POSITION = [(MY_POSITION[POS_X] + 1) % MAP_WIDTH, MY_POSITION[POS_Y]]
    elif direction == "q":
        break

    if NEW_POSITION:
        if OBSTACLES_DEFINITION[NEW_POSITION[POS_Y]][NEW_POSITION[POS_X]] != "#":
            TAIL.insert(0, MY_POSITION.copy())
            TAIL = TAIL[:TAIL_LEN]
            MY_POSITION = NEW_POSITION

    os.system("cls")
