import actions as a
#This file is used for getting commands from the user

def enterCommand(player, world):
    userInput = input(">>> ").lower()
    splitInput = userInput.split(" ", 1)
    splitInput.append(False) #We do this so functions with no args are still passed something

    valid = False
    for func in a.allCommands:
        if func.__name__ == splitInput[0]:
            valid = True
            return func(player, world, splitInput[1])
    if not valid :
        raise ValueError()
