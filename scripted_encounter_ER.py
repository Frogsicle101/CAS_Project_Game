from GUI import *
import scripted_encounter_main

def scripted_encounter_runner():

    if scripted_encounter_main.ER == 0:
        output("Sitting behind a large, wooden desk with a rotting, wormy apple atop it, is your English teacher. Ms. Kassandra. But she looks...different. \nWhere her legs once were, are the hind quarters of a lion. Sprouting from her back are wings like that of an eagle. \nMost odd though, is that she's wearing a sweater that doesn't age her appearance twenty years. Welcome to class! I hope you're ready to dive right back into classic literature!\n")
        c1 = scripted_encounter_main.choice(["Whatever", "Sure!", "What..happned to you?", "What's wrong wtih everyone here?"])
        scripted_encounter_main.ER = 1
        if c1==0:
            output("\nWell that's not very polite!\n" )
        elif c1==1:
            output("\nExcellent!\n")
        elif c1==2:
            output("\nIf you had paid attention in class recently, you'd know I am a sphinx, a creature out of the muths of Ancient Greece! Now, who is ready to dive back into the classics!?\n")
            c1 = scripted_encounter_main.choice(["Whatever", "Sure!"])

        output("Well, let's begin. Today's lesson will be a practical lesson on a common element in all mythology: riddles! \nMs. Kassandra's cheerful tone switched to one of grim foreboding as she looks regretfully towards the skeletons sitting at the desks. I hope you try harder than your peers.\n")


        counter = 2
        output("Here's your first riddle, from ancient Sumeria!\n\nThere is a house. One enters it blind and comes out seeing. What is it?\n")
        while counter>-1 and counter<3:
            answerList = ["school", "a school", "a schoolhouse", "schoolhouse\n" ]
            output("Type your guess: ")
            stringI = getInput()
            if stringI.lower() in answerList:
                output("\nWell done, but that was just the first riddle. Brace yourself!\n\n")
                counter = 6
            else:
                output("\nNope! Try again! You have "+str(counter)+" guesses left for this riddle!\n")
                counter = counter-1
                if counter == -1:
                    output("combat")
        output("Greek philosophy is where this next riddles comes from!\n\nThere is one father and twelve children;\nof these each Has twice thirty daughters of different appearance:\nSome are white to look at and the others black in turn;\nThey are immortal and yet they all fade away.\n")
        while counter>3 and counter<7:
            answerList = ["year", "a year", "the year", ]
            output("Type your guess: ")
            stringI = getInput()
            if stringI.lower() in answerList:
                output("\nImpressive, but don't get overconfident!\n\n")
                counter = 10
            else:
                output("\nNope! Try again! You have "+str(counter-4)+" guesses left for this riddle!\n")
                counter = counter-1
                if counter == 3:
                    output("combat")
        output("Your third and final riddle was supposedly made by Odin, Allfather of the Norse pantheon!\n\nFour hang, four sprang, two point the way, two to ward off dogs, one dangles after, always rather dirty. What am I?")
        while counter>7 and counter<11:
            answerList = ["cow", "a cow", "cows", ]
            output("Type your guess: ")
            stringI = getInput()
            if stringI.lower() in answerList:
                counter = 12
            else:
                output("\nNope! Try again! You have "+str(counter-8)+" guesses left for this riddle!\n")
                counter = counter-1
                if counter == 7:
                    output("combat")
