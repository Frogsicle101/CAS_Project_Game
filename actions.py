#This file stores all the possible actions that a player can do



def close(args):
    """Ends the program"""
    print("Hello")
    exit()

def teleport(args):
    """Allows the user to teleport around"""
    try:
        testX = int(args.split(" ")[0])
        testY = int(args.split(" ")[1])
        if world[testX][testY].getOpen():
            x = testX
            y = testY
            inputValid = True
        else:
            print("Room is locked")
    except IndexError():
        print("Out of range")

allCommands = [close]
