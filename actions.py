#This file stores all the possible actions that a player can do
import entities


def close(player, world, args):
    """Ends the program"""
    print("\n\nThank you for playing")
    exit()

def teleport(player, world, args):
    """Allows the user to teleport around"""
    try:
        if world[int(args.split(",")[0])][int(args.split(",")[1])].getOpen():
            player.position = [
                                int(args.split(",")[0]),
                                int(args.split(",")[1])
                                ]
        else:
            print("Room is locked")
    except ValueError:
        print("Out of range")

def go(player, world, args):
    """Allows the player to move around the world"""
    try:
        if args == "north":
            player.position[0] = player.position[0] - 1
        elif args == "south":
            player.position[0] = player.position[0] + 1
        elif args == "east":
            player.position[1] = player.position[1] + 1
        elif args == "west":
            player.position[1] = player.position[1] - 1
    except ValueError:
        print("You can't go that way")



def attack(player, world):
    for thing in world[player.position[0]][player.position[1]].getContained():
        if type(thing) is entities.Enemy:
            target = thing
    player.attack(target)

normalCommands = [teleport, close, go]
combatCommands = [attack]
