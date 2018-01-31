#The main game world
import rooms as tile

world = [tile.Corridor(False), tile.OtherRoom(False)]

while True:
    entry = input("0 or 1")
    if entry == "die":
        break
    entry = int(entry)
    print(world[entry].introText)
