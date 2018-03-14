#This file stores all the possible actions that a player can do



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

allCommands = [teleport, close]
