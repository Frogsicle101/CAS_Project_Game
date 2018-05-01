import actions as a
#This file is used for getting commands from the user

def enterCommand(player, world, inCombat):
    userInput = input(">>> ").lower()
    splitInput = userInput.split(" ", 1)

    valid = False
    for func in a.normalCommands:
        if func.__name__ == splitInput[0]:
            valid = True
            try:
                return func(player, world, splitInput[1].lower())
            except IndexError:
                return func(player, world)
            break
    else:
        for func in a.combatCommands:
            if func.__name__ == splitInput[0]:
                return func(player, world)


    if not valid :
        raise ValueError()
