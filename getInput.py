import actions as a
import GUI
#This file is used for getting commands from the user

def enterCommand(player, world):
    userInput = GUI.getInput().lower()
    splitInput = userInput.split(" ", 1)

    valid = False
    for action in a.normalCommands:
        if splitInput[0] in action.commands:
            valid = True
            try:
                return action.action(splitInput[1])
            except IndexError:
                return action.action()
            break


    if not valid :
        raise ValueError()
