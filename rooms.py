class Room:
    """Generic class for all rooms"""
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

class CorridorStrange(Room):
    def introText(self):
        return """You are in a corridor. But why do the walls seems to move?"""

class IceAgeRoom(Room):
    def introText(self):
        return """You step outside onto an expanse of brittle ice. Snowstorms surround you. A faint light can be seen in the distance."""

class WinRoom(Room):
    def __init__(self, contained):
        super().__init__(contained)
        self.open = False

    def introText(self):
        return """You win"""
