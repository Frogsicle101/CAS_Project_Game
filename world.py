#The main game world
import rooms as tile
import interactive as lever
import getInput
import players
import enemies
import items

def doThing():
    world[0][2].setOpen(True)

def play():
    stillPlaying = True
    thePlayer = players.Player(10, [0, 0], []) #creates player with nothing in inventory
    while stillPlaying:
        currentRoom = world[thePlayer.position[0]][thePlayer.position[1]]
        print("\n\n-------\nYou are at {}, {}".format(thePlayer.position[0], thePlayer.position[1]))
        print(currentRoom.introText())
        for thing in currentRoom.getContained():
            if type(thing) is enemies.Enemy:
                thePlayer.enterCombat(thing)

        inputValid = False
        while not inputValid:
            try:
                getInput.enterCommand(thePlayer, world)
                inputValid = True
            except ValueError:
                print("Invalid Input\n\n")

world = [
    [tile.Corridor([enemies.Enemy("Bad", 5, items.Weapon("Stick", 3, 3), 3)]), tile.DoorRoom([]), tile.WinRoom()],
    [tile.Corridor([])],
    [tile.OtherRoom([lever.Lever(doThing)])],
    [tile.Corridor([])]
    ]

play()
