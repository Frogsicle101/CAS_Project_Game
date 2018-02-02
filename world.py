#The main game world
import rooms as tile
import interactive as lever

def doThing():
    print("Hello")

world = [
    [tile.Corridor([]), tile.OtherRoom([])],
    [tile.Corridor([])],
    [tile.OtherRoom([lever.Lever(doThing)])]
    ]

while True:
    entry = input("0 or 1")
    currentRoom = world[2][0]
    if entry == "die":
        break
    elif entry == "pull lever":
        for object in currentRoom.getContained():
            if isinstance(object, lever.Lever):
                print("Test")
                object.getAction()
    else:
        entry = int(entry)
        position = ()
        print(world[entry].introText())
