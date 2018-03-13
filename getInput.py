import actions as a
#This file is used for getting commands from the user

userInput = input(">>> ").lower()
splitInput = userInput.split(" ", 1)


for func in a.allCommands:
    if func.__name__ == splitInput[0]:
        return func(splitInput)
    else:
        raise ValueError()
