from tkinter import *
import rooms as tile
import interactive as lever
import getInput
import entities
import items
import actions as a

import time
import copy


def runGame(*args):
    try:
        toBeOutputted = (enterCommand(thePlayer, world))
        if toBeOutputted != None:
            T.after(1000, lambda: output(toBeOutputted))
    except ValueError:
        output("Invalid")
    finally:
        currentRoom = world[thePlayer.position[0]][thePlayer.position[1]]
        global screenredindex
        screenredindex = (16 - thePlayer.health)//4
        root["bg"] = screenred[screenredindex]

        #Displays messages about situation to player
        T.after(1000, lambda: output("\n\n-------\nYou are at {}, {}".format(thePlayer.position[0], thePlayer.position[1])))
        T.after(1000, lambda: output(currentRoom.introText()))

    #run freddy code here()
    #if you take damage, i++ then root["bg"] = screenred[i], if you heal, i-- then root["bg"] = screenred[i]

def enterCommand(player, world):
    global inputTextBox
    userInput = inputTextBox.get().lower()
    inputTextBox.delete(0, END)
    splitInput = userInput.split(" ", 1)
    valid = False
    for func in a.normalCommands:
        if func.__name__ == splitInput[0]:
            valid = True

            try:
                return func(player, world, splitInput[1].lower())
            except IndexError:
                return func(player, world)
            break
    if not valid:
        raise ValueError()

def output(text):
    T.configure(state='normal')
    T.insert(END, text + "\n")
    T.see(END)
    T.configure(state="disabled")

b = '#000000'
br = '#550000'
rb = '#AA0000'
r = '#FF0000'
screenred= [b, br, rb, r]
global screenredindex
screenredindex = 0
root = Tk()

root.geometry("800x400")
root["bg"] = screenred[screenredindex]

S = Scrollbar(root)
T = Text(root, height=10, width=50)
S.pack(side=RIGHT, fill=Y)
#T.place(relx=.5, rely=.75, anchor="center")
#T.pack(side=BOTTOM)
S.config(command=T.yview)
T.config(yscrollcommand=S.set, state="disabled")
root.title('Name')

inputFrame = Frame(root, width=50)
inputFrame.pack(side=BOTTOM)
inputTextBox = Entry(inputFrame)
inputTextBox.focus_set()

b = Button(inputFrame,text='Enter',command=runGame)
root.bind('<Return>', runGame)


b.pack(side=RIGHT)
inputTextBox.pack(side=LEFT)
T.pack(side=BOTTOM)

thePlayer = entities.Player(16, [0, 0], [], 10) #creates player with nothing in inventory
output("""Welcome to the Game
We hope you have fun""")

weapon = items.Weapon("stabby", 5, 3)
steve = entities.Enemy("steve", 5, weapon, 2)

world = [
    [tile.Corridor([steve]), tile.DoorRoom([]), tile.WinRoom([])],
    [tile.Corridor([])],
    [tile.OtherRoom([])],
    [tile.Corridor([])]
    ]
currentRoom = world[thePlayer.position[0]][thePlayer.position[1]]

#Displays messages about situation to player
output("\n\n-------\nYou are at {}, {}".format(thePlayer.position[0], thePlayer.position[1]))
output(currentRoom.introText())

root.mainloop()
