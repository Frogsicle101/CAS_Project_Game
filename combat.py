#combat
from GUI import *

def enter(player, world, target):
    stillFighting = True
    while stillFighting:
        if target.isAlive():
            output("You are in combat with {}! Your Health:{}. Enemy Health:{}".format(target.name, player.health, target.health))

            inputValid = False
            while not inputValid:
                command = getInput().lower()
                inputValid = True
                if command == "attack":
                    player.attack(target)
                elif command == "flee":
                    stillFighting = False
                    player.flee()
                else:
                    output("Invalid Input\n\n")
                    inputValid = False
        else:
            stillFighting = False
            output("You have defeated {}! Your Health:{}".format(target.name, player.health))
