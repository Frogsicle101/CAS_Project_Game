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
    def __init__(self):
        super().__init__([])
        self.open = False

    def introText(self):
        return """You win"""

class StartingRoom(Room):
    def introText(self):
        return """You have been crammed into a locker for hours. Just another day at Sunnyvale High."""

class MUNRoom(Room):
    def introText(self):
        return """You find yourself entering a classroom
        with a row of nearly arrayed desks, each with a placard with a
        country's name and a flag."""

 class CodingClub(Room):
     def intoText(self):
         return """You enter a room that smells like the bottom of a chips packet. Dotted around the room
         are the faint hues of monitors. Behind those
         monitors, are the sunken faces of high-school
         coders."""

 class  Gym(Room):
     def intoText(self):
         return """Entering the gym, you are greeted with squeaky floors and a ceiling that's infinitely high."""

  class AnimeClub(Room):
      def introText(Self):
          return """Pushing open the door, you find yourself in a dark classroom. The only light in the room comes from a projector screen near the front of the classroom. On it, animated figures speak in rushed Japanese."""

  class EnglishRoom(Room):
      def introText(Self):
          return """You find yourself in a room covered in the scent of old carpet, creaky floorboards, and rancid coffee. The rancid coffee scent originates from a decaying blue mug. Holding that blue mug is the hook-nosed Ms. Crowley, your English teacher. """
