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
weapon = items.Weapon("stabby", 5, 1)
steve = entities.Enemy("steve", 5, weapon, 2)
fangs = items.Weapon("fangs", 5. 3)
Wolf = entities.Enemy("Wolf", 3, fangs, 2)
baseball_bat = Items.weapons("baseball bat", 5, 2)
Swatter = entities.Enemy("Swatter",4, baseball_bat, 2)
spiky_pom_poms = items.Weapon("spiky_pom_poms", 5, 3)
Cheerbleeder = entities.Enemy("Cheerbleeder", 4, spiky_pom_poms, 3)
spear = Items.Weapon("spear", 5, 3)
Gladiator = entities.Enemy("Gladiator",5, spear, 5)
broomstick = Items.weapon("broomstick", 5, 1)
Janitor = entities.Enemy("Janitor", 3, broomstick, 1 )
beak = Items.Weapon("beak", 0, 2)
Rabid_Penguin = entities.Enemy("Rabid Penguin", 2, beak, 5)
contorting_spear = Items.Weapon("contorting spear", 8, 6)
Monstrous_Gladiator = entities.Enemy("Monstrous Gladiator",8, spear, 7)
teeth = items.Weapon("teeth", 5. 3)
Tiger = entities.Enemy("Wolf", 5, teeth, 6)
appendage = items.Weapon("appendage",100, 7)
Shoggoth = entities.Enemy("Shoggoth", 10, appendage, 8)
plastic_katana = items.Weapon("plastic katana", 1, 0)
Weaboo = entities.Enemy("Weaboo", 2, plastic_katana, 1)
world = [
    [tile.Corridor([steve,  copy.deepcopy(steve)]), tile.DoorRoom([]), tile.IceAgeRoom([Wolf, copy.deepcopy(Wolf)])] tile.WinRoom([])],
    [tile.Corridor([])],
    [tile.IceAgeRoom([])],
    [tile.OtherRoom([])],
    [tile.Corridor([])]
    ]

play()
