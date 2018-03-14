#The class for the player character in the game.
class Player:
    def __init__(self, health, position, inventory):
        self.health = health #int
        self.position = position #list of two ints
        self.inventory = inventory #list of item objects
