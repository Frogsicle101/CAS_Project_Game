class Room:
    def __init__(self, contained):
        self.contained = contained

    def introText(self):
        raise NotImplementedError

    def getContained(self):
        return self.contained

class Corridor(Room):
    def introText(self):
        return """You are in a corridor"""

class OtherRoom(Room):
    def introText(self):
        return """You are in some random other room"""
