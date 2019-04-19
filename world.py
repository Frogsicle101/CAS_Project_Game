#The main game world
import rooms as tile
import entities
import items


#The main game world. All information about everything is stored here. Do not delete
weapon = items.Weapon("stabby", 5, 1)
steve = entities.Enemy("steve", 5, weapon, 2)
fangs = items.Weapon("fangs", 5, 3)
Wolf = entities.Enemy("Wolf", 3, fangs, 2)
baseball_bat = items.Weapon("baseball bat", 5, 2)
Swatter = entities.Enemy("Swatter",4, baseball_bat, 2)
spiky_pom_poms = items.Weapon("spiky_pom_poms", 5, 3)
Cheerbleeder = entities.Enemy("Cheerbleeder", 4, spiky_pom_poms, 3)
spear = items.Weapon("spear", 5, 3)
Gladiator = entities.Enemy("Gladiator",5, spear, 5)
broomstick = items.Weapon("broomstick", 5, 1)
Janitor = entities.Enemy("Janitor", 3, broomstick, 1 )
beak = items.Weapon("beak", 0, 2)
Rabid_Penguin = entities.Enemy("Rabid Penguin", 2, beak, 5)
contorting_spear = items.Weapon("contorting spear", 8, 6)
Monstrous_Gladiator = entities.Enemy("Monstrous Gladiator",8, spear, 7)
teeth = items.Weapon("teeth", 5, 3)
Tiger = entities.Enemy("Wolf", 5, teeth, 6)
appendage = items.Weapon("appendage",100, 7)
Shoggoth = entities.Enemy("Shoggoth", 10, appendage, 8)
plastic_katana = items.Weapon("plastic katana", 1, 0)
Weaboo = entities.Enemy("Weaboo", 2, plastic_katana, 1)
world = [
    [tile.EnglishRoom([]), tile.DoorRoom([]), tile.IceAgeRoom([])],
    [tile.Corridor([])],
    [tile.IceAgeRoom([])],
    [tile.OtherRoom([])],
    [tile.Corridor([])]
    ]

#play()
