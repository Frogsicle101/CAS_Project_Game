from tkinter import *
from tkinter import messagebox
import time
import copy
import exceptions


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
    userInput = getGUIInput()
    splitInput = userInput.split(" ", 1)
    valid = False
    for func in a.normalCommands:
        if func.__name__ == splitInput[0]:
            valid = True
            return func(player, world, splitInput[1])
            break
    if not valid:
        raise ValueError()

buttonPressed = False
userInput = ""
endingBool = False

def getInput():
    global buttonPressed
    buttonPressed = False
    global userInput
    userInput = ""

    while not buttonPressed and not endingBool:
        root.update()
    if endingBool:
        root.destroy()
        exit()
    return userInput

def press():
    global buttonPressed
    buttonPressed = True
    global inputTextBox
    global userInput
    userInput = inputTextBox.get().lower()
    inputTextBox.delete(0, END)

def output(text, *args):

    counter = 0
    newText = ""
    for char in text:
        if counter > 40 and char == " ":
            newText += "\n"
            counter = 0
        else:
            newText += char
        counter += 1
    text = newText

    T.configure(state='normal')
    T.insert(END, text)

    #If the first arg is True, or is not given, we append a newline
    #otherwise, do not append
    try:
        if args[0]:
            T.insert(END, "\n")
    except IndexError:
        T.insert(END, "\n")

    T.see(END)
    T.configure(state="disabled")
    root.update()

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
root.title("Game")

S = Scrollbar(root)
T = Text(root, height=10, width=50)
S.pack(side=RIGHT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set, state="disabled")

inputFrame = Frame(root, width=50)
inputFrame.pack(side=BOTTOM)
inputTextBox = Entry(inputFrame)
inputTextBox.focus_set()

b = Button(inputFrame,text='Enter',command=press)
root.bind('<Return>', lambda event: press()) #Ignore event


b.pack(side=RIGHT)
inputTextBox.pack(side=LEFT)
T.pack(side=BOTTOM)

def closing():
    global endingBool
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        endingBool = True
root.protocol("WM_DELETE_WINDOW", closing)
