import os
import readchar
import random


POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
MY_POSITION = [8,4]
NUMBER_OF_OBJECTS = 11
TAIL_LEN = 0
TAIL = []
MAP_OBJECTS = []
END_GAME = False

#Generate random objects in map
while len(MAP_OBJECTS) < NUMBER_OF_OBJECTS:
    NEW_POSITION = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

    if NEW_POSITION not in MAP_OBJECTS and NEW_POSITION != MY_POSITION:
        MAP_OBJECTS.append(NEW_POSITION)

#Main Loop
while END_GAME == False:
    #DrawMap
    print("+" + "-" * (MAP_WIDTH * 3) + "-" + "+")

    for CORDINATE_Y in range(MAP_HEIGHT):
        print("|", end=" ")

        for CORDINATE_X in range(MAP_WIDTH):

            CHAR_TO_DRAW = " "
            OBJECT_IN_CELL = None

            for MAP_OBJECT in MAP_OBJECTS:
                if MAP_OBJECT[POS_X] == CORDINATE_X and MAP_OBJECT[POS_Y] == CORDINATE_Y:
                    CHAR_TO_DRAW = "*"
                    OBJECT_IN_CELL = MAP_OBJECT
            for TAIL_PIECE in TAIL:
                if TAIL_PIECE[POS_X] == CORDINATE_X and TAIL_PIECE[POS_Y] == CORDINATE_Y:
                    CHAR_TO_DRAW = "@"
            if MY_POSITION in TAIL:
                print("YOU LOSE!")
                exit()
            elif MY_POSITION[POS_X] == CORDINATE_X and MY_POSITION[POS_Y] == CORDINATE_Y:
                CHAR_TO_DRAW = "@"
                if OBJECT_IN_CELL:
                    MAP_OBJECTS.remove(OBJECT_IN_CELL)
                    TAIL_LEN += 1

            print(" {} ".format(CHAR_TO_DRAW), end="")
        print("|")
    print("+" + "-" * (MAP_WIDTH * 3) + "-" + "+")

    # Ask user where he wants to move
    #direction = input("¿Donde te quieres mover? WASD: ")
    direction = readchar.readchar().decode()

    if direction == "w":
        TAIL.insert(0, MY_POSITION.copy())
        TAIL = TAIL[:TAIL_LEN]
        MY_POSITION[POS_Y] -= 1
        MY_POSITION[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        TAIL.insert(0, MY_POSITION.copy())
        TAIL = TAIL[:TAIL_LEN]
        MY_POSITION[POS_Y] += 1
        MY_POSITION[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        TAIL.insert(0, MY_POSITION.copy())
        TAIL = TAIL[:TAIL_LEN]
        MY_POSITION[POS_X] -= 1
        MY_POSITION[POS_X] %= MAP_WIDTH
    elif direction == "d":
        TAIL.insert(0, MY_POSITION.copy())
        TAIL = TAIL[:TAIL_LEN]
        MY_POSITION[POS_X] += 1
        MY_POSITION[POS_X] %= MAP_WIDTH
    elif direction == "q":
        break
    os.system("cls")

