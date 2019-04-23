from GUI import *

options = ["1. ", "2. ", "3. "]

LO = 0
ER = 0
HI = 0
SC = 0
FH = 0
PR = 0


#used to display options
def choice(options):
    x = 1
    for option in options:
        output(str(x)+" "+str(option))
        x = x+1


    #used to read user input and porcess response
    output("Enter the number associated with your desired response: ")
    x = int(getInput())
    for idx, val in enumerate(options):
        if idx == x-1:
            return idx
            output(str(idx))
