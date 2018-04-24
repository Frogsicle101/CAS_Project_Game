import random
import items

#The base class for all entities in the game
class Entity:

    def __init__(self, health, skill):
        self.health = health
        self.skill = skill

    def takeDamage(self, amount):
        self.health -= amount

    def isAlive(self):
        return self.health > 0

    def attack(self, target):
        if random.randint(0, 9) < self.skill:
            target.takeDamage(self.weapon.damage)

class Player(Entity):
    def __init__(self, health, position, inventory, skill):
        self.position = position #list of two ints
        self.inventory = inventory #list of item objects
        super().__init__(health, skill)

    def enterCombat(self, enemy):
        while self.isAlive() and enemy.isAlive():
            print("You are in combat with {}! Your Health:{}. Your Enemy {}".format(enemy.name, self.health, enemy.health))
            entry = input(">>>")
            if entry == "Attack":
                self.attack(enemy)
            enemy.attack(self)




#Enemies
class Enemy(Entity):
    def __init__(self, name, health, weapon, skill):
        self.name = name
        self.weapon = weapon
        super().__init__(health, skill)
