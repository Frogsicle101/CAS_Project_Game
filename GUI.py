from tkinter import *
def printtext():
    global e
    string = e.get()
    e.

b = '#000000'
br = '#550000'
rb = '#AA0000'
r = '#FF0000'
screenred= [b, br, rb, r]
i = 0
root = Tk()

root.geometry("800x400")
root["bg"] = screenred[i]
S = Scrollbar(root)
T = Text(root, height=10, width=50)
S.pack(side=RIGHT, fill=Y)
T.place(relx=.5, rely=.75, anchor="center")
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
root.title('Name')

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='okay',command=printtext)
b.pack(side='bottom')

    #run freddy code here()
    #if you take damage, i++, if you heal, i--

root.mainloop()
