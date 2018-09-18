#The main game world
import rooms as tile
import interactive as lever
import getInput
import entities
import items

import time
import copy

def play():
    """The main method that runs the entire game"""
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
    """Prints all items and entities in the room passed to it"""
    print("There is: ", end="")
    for i, thing in enumerate(currentRoom.contained):
        if type(thing) is entities.Enemy:
            if thing.isAlive():
                print(thing.name + "[Alive]", end="")
            else:
                print(thing.name + "[Dead]", end="")
        else:
            print(thing.name, end="")
        if i + 1 != len(currentRoom.contained):
            print(", ", end="")
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
