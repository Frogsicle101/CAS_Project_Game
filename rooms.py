class Room:
    def __init__(self, contained):
        self.contained = contained
        self.open = True

    def introText(self):
        raise NotImplementedError

class Corridor(Room):
    def introText(self):
        return """You are in a corridor"""

class OtherRoom(Room):
    def introText(self):
        return """You are in some random other room"""

class DoorRoom(Room):
    def introText(self):
        return """You are in a room with a large imposing door"""

class IceRoom(Room):
    def introText(self):
        return """You seem to be outside, in a frozen tundra. But how can that be?"""

class StrangeCorridor(Room):
    def introText(self):
        return """You are in a corridor, yet it seems that the walls shift in your peripheral vision."""


class WinRoom(Room):
    def __init__(self, contained):
        super().__init__(contained)
        self.open = False

    def introText(self):
        return """You win"""
