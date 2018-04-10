#items
class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value
class Weapon(Item):
    def __init__(self, name, value, damage):
        self.damage = damage
        super().__init__(name, value)
