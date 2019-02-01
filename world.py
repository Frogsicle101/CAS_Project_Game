#The main game world
import rooms as tile
import entities
import items


#The main game world. All information about everything is stored here. Do not delete
weapon = items.Weapon("stabby", 5, 3)
steve = entities.Enemy("steve", 5, weapon, 2)
world = [
    [tile.Corridor([steve]), tile.DoorRoom([]), tile.WinRoom([])],
    [tile.Corridor([])],
    [tile.OtherRoom([])],
    [tile.Corridor([])]
    ]

#play()
