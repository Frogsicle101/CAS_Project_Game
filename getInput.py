import actions as a
import GUI
#This file is used for getting commands from the user

def enterCommand(player, world):
    userInput = GUI.getInput().lower()
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


    if not valid :
        raise ValueError()
