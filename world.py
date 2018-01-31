#The main game world
import rooms as tile

world = [tile.Corridor(), tile.OtherRoom]

while True:
    entry = input("0 or 1")
    print(world[i].introText)
