#The main game world
import rooms as tile
import interactive as lever

def doThing():
    world[0][2].setOpen(True)

def play():
    stillPlaying = True
    x = 0
    y = 0
    while stillPlaying:
        currentRoom = world[x][y]
        print("\n\n-------\nYou are at {}, {}".format(x, y))
        print(currentRoom.introText())

        inputValid = False
        while not inputValid:
            entry = input(">>> ").lower()
            if entry == "quit":
                inputValid = True
                stillPlaying = False
            elif entry.split(" ")[0].lower() == "teleport":
                try:
                    x = int(entry.split(" ")[1])
                    y = int(entry.split(" ")[2])
                    inputValid = True
                except IndexError():
                    print("Out of range")
            elif entry == "pull lever":
                for object in currentRoom.getContained():
                    if isinstance(object, lever.Lever):
                        object.getAction()
                        inputValid = True




world = [
    [tile.Corridor([]), tile.DoorRoom([]), tile.WinRoom()],
    [tile.Corridor([])],
    [tile.OtherRoom([lever.Lever(doThing)])],
    [tile.Corridor([])]
    ]

play()
