#The main game world
import rooms as tile
import interactive as lever
import getInput
import entities
import items

import time

def play():
    stillPlaying = True
    thePlayer = entities.Player(10, [0, 0], [], 10) #creates player with nothing in inventory
    while stillPlaying:

        currentRoom = world[thePlayer.position[0]][thePlayer.position[1]]

        #Displays messages about situation to player
        print("\n\n-------\nYou are at {}, {}".format(thePlayer.position[0], thePlayer.position[1]))
        print(currentRoom.introText())
        displayContained(currentRoom)

        #Gets user input
        inputValid = False
        while not inputValid:
            try:
                getInput.enterCommand(thePlayer, world)
                inputValid = True
            except ValueError:
                print("Invalid Input\n\n")
        time.sleep(1)


def displayContained(currentRoom):
    print("There is: ", end="")
    for thing in currentRoom.contained:
        print(thing.name, end=", ")
    print(" here")

#The main game world. All information about everything is stored here. Do not delete
weapon = items.Weapon("stabby", 5, 3)
steve = entities.Enemy("steve", 5, weapon, 2)
world = [
    [tile.Corridor([steve]), tile.DoorRoom([]), tile.WinRoom([])],
    [tile.Corridor([])],
    [tile.OtherRoom([])],
    [tile.Corridor([])]
    ]

play()
