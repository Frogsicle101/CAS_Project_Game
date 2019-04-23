#This is the main file
from GUI import *

from world import world
import rooms as tile
import interactive as lever
import getInput
import entities
import items

import time
import copy

import exceptions



def play():
    stillPlaying = True
    thePlayer = entities.Player(16, [0, 0], [], 10)

    while stillPlaying:
        playTurn(thePlayer, world)

def playTurn(thePlayer, world):
    currentRoom = world[thePlayer.position[0]][thePlayer.position[1]]

    def displayRoom(room):
        def displayContained(room):
            """Prints all items and entities in the room passed to it"""
            output("There is: ", False)
            for i, thing in enumerate(currentRoom.contained):
                if type(thing) is entities.Enemy:
                    if thing.isAlive():
                        output(thing.name + "[Alive]", False)
                    else:
                        output(thing.name + "[Dead]", False)
                else:
                    output(thing.name, False)
                if i + 1 != len(currentRoom.contained):
                    output(", ", False)


            output(" here")
        output("\n\n-------\nYou are at {}, {}".format(thePlayer.position[0], thePlayer.position[1]))
        output(room.introText())
        if len(room.contained) > 0:
            displayContained(room)


    inputValid = False
    while not inputValid:
        try:
            displayRoom(currentRoom)
            output("-"*50)
            getInput.enterCommand(thePlayer, world)
            inputValid = True
        except exceptions.InvalidInput as e:
            output("Invalid Input: " + str(e))
play()
