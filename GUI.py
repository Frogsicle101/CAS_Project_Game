from tkinter import *
def output(text):
    textin = text

def getCurrentLine():
    return T.get("end-1l","end-1c")

def getPreviousLine():
    return T.get("end-2l","end-1c1l")
b = '#000000'
br = '#550000'
rb = '#AA0000'
r = '#FF0000'
screenred=rb
i = 1
dogamerun = True
root = Tk()

root.geometry("800x400")
root["bg"] = screenred
S = Scrollbar(root)
T = Text(root, height=10, width=50)
S.pack(side=RIGHT, fill=Y)
T.place(relx=.5, rely=.75, anchor="center")
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
T.insert(END, "\n\n")
if getCurrentLine() =="" and getPreviousLine() != "":
    #pass freddy threeput()
    i = i
def print(input):
    T.insert(END, input + "  \n  \n")
root.mainloop()
