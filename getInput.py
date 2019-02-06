import actions as a
import GUI
import exceptions
#This file is used for getting commands from the user

def enterCommand(player, world):
    userInput = GUI.getInput().lower()
    splitInput = userInput.split(" ", 1)

    found = False
    for action in a.normalCommands:
        if splitInput[0] in action.commands:
            found = True
            try:
                return action.action(player, world, splitInput[1])
            except IndexError:
                return action.action(player, world)
            break

    if not found:
        raise exceptions.InvalidInput("Command not found")
