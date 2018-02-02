class Interactable:
    def __init__(self, name, canpush, dsc, pickup):
        self.name=name
        self.canpush=canpush
        self.dsc=dsc
        self.pickup=pickup
lockerDoor=Interactable("locker door", "true", "It is a red, metal door with some grates near the top, standard across all of Brockton High School", "false")
class Room:
    def __init__(self, x, y, dsc):
        self.x = x
        self.y = y
        self.dsc=dsc
room1=Room(0,0,"You open your eyes, but all you can see is the inside of the locker those bullies stuffed you in. What's strange is that you can't hear anyone in the halls? How long were you in there?")
room2=Room(0,1,"Emerging from your locker, you can see that the hallway is completely deserted, and the hallway lights are flickering on and off. To the north, is the Stairway up to the Second Floor, to the south is the High School Entrance. ")
print(room1.dsc)
response=input("\nWhat would you like to do?\n")
if response=="push locker door":
    print("You kick against the locker door with your feet, and eventually you are able to kick it open.\n")
    print(room2.dsc)
else:
    print("Sorry, you can't do that.")
