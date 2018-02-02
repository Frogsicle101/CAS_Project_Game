class Room:
    def __init__(self, contained):
        self.contained = contained
        self.open = False

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

class DoorRoom(Room):
    def introText(self):
        return """You are in a room with a large imposing door"""

class WinRoom(Room):
    def introText(self):
        return """You win"""
