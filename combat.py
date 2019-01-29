#combat
#import GUI

def enter(player, world, target):
    stillFighting = True
    while stillFighting:
        if target.isAlive():
            print("You are in combat with {}! Your Health:{}. Enemy Health:{}".format(target.name, player.health, target.health))

            inputValid = False
            while not inputValid:
                command = GUI.getGUIInput(">>>").lower()
                inputValid = True
                if command == "attack":
                    player.attack(target)
                elif command == "flee":
                    stillFighting = False
                    player.flee()
                else:
                    print("Invalid Input\n\n")
                    inputValid = False
        else:
            stillFighting = False
            print("You have defeated {}! Your Health:{}".format(target.name, player.health))
