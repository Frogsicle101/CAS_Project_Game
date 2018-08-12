#The main game world
import rooms as tile
import interactive as lever
import getInput
import entities
import items

def doThing():
    world[0][2].setOpen(True)

def play():
    stillPlaying = True
    thePlayer = entities.Player(10, [0, 0], [], 10) #creates player with nothing in inventory
    while stillPlaying:
        inCombat = False

        currentRoom = world[thePlayer.position[0]][thePlayer.position[1]]


        #Checks if enemies present in current room
        for thing in currentRoom.getContained():
            if type(thing) is entities.Enemy:
                inCombat = True
                enemy = thing

        #Displays messages about situation to player
        print("\n\n-------\nYou are at {}, {}".format(thePlayer.position[0], thePlayer.position[1]))
        if inCombat:
            print("You are in combat with {}! Your Health:{}. Enemy Health:{}".format(enemy.name, thePlayer.health, enemy.health))
        else:
            print(currentRoom.introText())

        #Gets user input
        inputValid = False
        while not inputValid:
            try:
                getInput.enterCommand(thePlayer, world, inCombat)
                inputValid = True
            except ValueError:
                print("Invalid Input\n\n")


#The main game world. All information about everything is stored here. Do not delete
world = [
    [tile.Corridor([]), tile.DoorRoom([]), tile.WinRoom()],
    [tile.Corridor([])],
    [tile.OtherRoom([lever.Lever(doThing)])],
    [tile.Corridor([])]
    ]

play()
