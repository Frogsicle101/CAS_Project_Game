#The main game world
import rooms as tile
import interactive as lever
import getInput
import players

def doThing():
    world[0][2].setOpen(True)

def play():
    stillPlaying = True
    thePlayer = players.Player(10, [0, 0], []) #creates player with nothing in inventory
    while stillPlaying:
        currentRoom = world[thePlayer.position[0]][thePlayer.position[1]]
        print("\n\n-------\nYou are at {}, {}".format(thePlayer.position[0], thePlayer.position[1]))
        print(currentRoom.introText())
        inputValid = False
        while not inputValid:
            try:
                getInput.enterCommand(thePlayer, world)
                inputValid = True
            except ValueError:
                print("Invalid Input\n\n")














            """entry = input(">>> ").lower()
            if entry == "quit":
                inputValid = True
                stillPlaying = False
            elif entry.split(" ")[0].lower() == "teleport":
                try:
                    testX = int(entry.split(" ")[1])
                    testY = int(entry.split(" ")[2])
                    if world[testX][testY].getOpen():
                        x = testX
                        y = testY
                        inputValid = True
                    else:
                        print("Room is locked")
                except IndexError():
                    print("Out of range")
            elif entry == "pull lever":
                for object in currentRoom.getContained():
                    if isinstance(object, lever.Lever):
                        object.getAction()
                        inputValid = True"""




world = [
    [tile.Corridor([]), tile.DoorRoom([]), tile.WinRoom()],
    [tile.Corridor([])],
    [tile.OtherRoom([lever.Lever(doThing)])],
    [tile.Corridor([])]
    ]

play()
