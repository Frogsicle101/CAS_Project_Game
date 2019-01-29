#This file stores all the possible actions that a player can do
import entities
import copy
import combat


def close(player, world):
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

def go(inputPlayer, world, args):
    """Allows the player to move around the world"""
    player = copy.deepcopy(inputPlayer)
    args = args.lower()
    try:
        if args == "north":
            player.position[0] -= 1
        elif args == "south":
            player.position[0] += 1
        elif args == "east":
            player.position[1] += 1
        elif args == "west":
            player.position[1] -= 1
        assert(player.position[0] >= 0 and player.position[1] >= 0)
        world[player.position[0]][player.position[1]]
    except(AssertionError, IndexError):
        return "You can't go that way"
    else:
        inputPlayer.position = player.position

def fight(player, world, args):
    foundTarget = False
    for thing in world[player.position[0]][player.position[1]].contained:
        if type(thing) is entities.Enemy and args == thing.name and thing.isAlive():
            foundTarget = True
            target = thing

    if foundTarget:
        combat.enter(player, world, target)
    else:
        print(args + " cannot be attacked")


normalCommands = [teleport, close, go]
