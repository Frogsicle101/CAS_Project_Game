from tkinter import *
def runGame():
    global inputTextBox
    string = inputTextBox.get()
    string = string.lower()
    print (string)
    inputTextBox.delete(0, END)
    #run freddy code here()
    #if you take damage, i++ then root["bg"] = screenred[i], if you heal, i-- then root["bg"] = screenred[i]

def textIn(text);
    global T
    T.insert(END, text+"\n")
    
b = '#000000'
br = '#550000'
rb = '#AA0000'
r = '#FF0000'
screenred= [b, br, rb, r]
screenredindex = 0
root = Tk()

root.geometry("800x400")
root["bg"] = screenred[screenredindex]

S = Scrollbar(root)
T = Text(root, height=10, width=50)
S.pack(side=RIGHT, fill=Y)
T.place(relx=.5, rely=.75, anchor="center")
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
root.title('Name')

inputTextBox = Entry(root)
inputTextBox.pack()
inputTextBox.focus_set()

b = Button(root,text='Enter',command=runGame)
b.pack(side='bottom')

root.mainloop()
