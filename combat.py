#combat

def enter(player, world, target):
    while True:
        print("You are in combat with {}! Your Health:{}. Enemy Health:{}".format(target.name, player.health, target.health))

        inputValid = False
        while not inputValid:
            command = input(">>>").lower()
            inputValid = True
            if command == "attack":
                player.attack(target)
            elif command == "flee":
                flee()
            else:
                print("Invalid Input\n\n")
                inputValid = False
