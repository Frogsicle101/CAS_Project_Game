#This file stores all the possible actions that a player can do
import entities
import copy
import combat
import exceptions
import GUI

class Action:
    commands = []
    def __init__(self, commands, action):
        self.commands = commands
        self.action = action
    def action(*args):
        raise NotImplementedError()


close = Action(["close", "exit", "end"], lambda *args: exit())

def teleportAction(*args):
    player = args[0]
    world = args[1]
    coords = args[2].split(",")
    try:
        x = int(coords[0])
        y = int(coords[1])
    except(ValueError, IndexError):
        raise exceptions.InvalidInput("Co-ords for teleport should be in the form x,y")

    """Allows the user to teleport around"""
    try:
        if world[x][y].open:
            player.position = [x, y]
        else:
            GUI.output("Room is locked")
    except (ValueError, IndexError):
        GUI.output("Out of range")
teleport = Action(["teleport", "tp"], teleportAction)

def goAction(*args):
    """Allows the player to move around the world"""

    inputPlayer = args[0]
    world = args [1]
    direction = args[2]

    player = copy.deepcopy(inputPlayer)
    try:
        if direction == "north":
            player.position[0] -= 1
        elif direction == "south":
            player.position[0] += 1
        elif direction == "east":
            player.position[1] += 1
        elif direction == "west":
            player.position[1] -= 1
        else:
            raise exceptions.InvalidInput("Use 'North', 'South', 'East', or 'West'")
        assert(player.position[0] >= 0 and player.position[1] >= 0)
        world[player.position[0]][player.position[1]]
    except(AssertionError, IndexError):
        GUI.output("You can't go that way")
    else:
        inputPlayer.previousPosition = inputPlayer.position
        inputPlayer.position = player.position
go = Action(["go", "move", "travel", "walk"], goAction)

def fightAction(*args):
    player = args[0]
    world = args[1]
    selectedTarget = args[2]

    foundTarget = False
    for thing in world[player.position[0]][player.position[1]].contained:
        if type(thing) is entities.Enemy and selectedTarget == thing.name and thing.isAlive():
            foundTarget = True
            target = thing

    if foundTarget:
        combat.enter(player, world, target)
    else:
        GUI.output(selectedTarget + " cannot be attacked")
fight = Action(["fight", "attack", "combat"], fightAction)

normalCommands = [close, teleport, go, fight]
