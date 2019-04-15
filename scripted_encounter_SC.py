import scripted_encounter_main
ER = false
if ER == false:
    print("Pacing the front of the room is someone who must be your science teacher, Mr. Pitters, but he's now 1 foot shorter, covered in green skin, and has a scrunched up, rat-like face. In his hands are vials full of frothing, exotically colored liquids. He looks at you, mania dancing in his eyes, his teeth bared in a hungry leer. On his desk, next to a stack of papers, . 'Are you ready for your chemistry assignment?'\n")
    c1 = scripted_encounter_main.choice(["Okay", "No?", "You look unusally good today Mr. Pitters.", "What are you supposed to be?"])
    ER = true
    if c1==0:
        print("\nExcellent!\n" )
    elif c1==1:
        print("\nToo bad, you're here now.\n")
    elif c1==2:
        print("\nI'll let that one slide, since today's assignment must be quite nerve wracking for students of your caliber.")
    elif c1==3:
        print("\nLost your memory? Hope you haven't forgotten your chemicals! I'm Mr. Pitters, your favorite chemistry teacher!")
        c1 = scripted_encounter_main.choice(["Whatever", "Sure!"])

    print("Your assignment is simple, make something in the lab that I'll remember for the rest of my life, something truly special. You have until school's out\n")


    counter = 2
    print("Here's your first riddle, from ancient Sumeria!\n\nThere is a house. One enters it blind and comes out seeing. What is it?\n")
    while counter>-1 and counter<3:
        answerList = ["school", "a school", "a schoolhouse", "schoolhouse" ]
        stringI = input("Type your guess: ")
        if stringI.lower() in answerList:
            print("\nWell done, but that was just the first riddle. Brace yourself!\n\n")
            counter = 6
        else:
            print("\nNope! Try again! You have "+str(counter)+" guesses left for this riddle!\n")
            counter = counter-1
            if counter == -1:
                print("combat")
    print("Greek philosophy is where this next riddles comes from!\n\nThere is one father and twelve children;\nof these each Has twice thirty daughters of different appearance:\nSome are white to look at and the others black in turn;\nThey are immortal and yet they all fade away.\n")
    while counter>3 and counter<7:
        answerList = ["year", "a year", "the year", ]
        stringI = input("Type your guess: ")
        if stringI.lower() in answerList:
            print("\nImpressive, but don't get overconfident!\n\n")
            counter = 10
        else:
            print("\nNope! Try again! You have "+str(counter-4)+" guesses left for this riddle!\n")
            counter = counter-1
            if counter == 3:
                print("combat")
    print("Your third and final riddle was supposedly made by Odin, Allfather of the Norse pantheon!\n\nFour hang, four sprang, two point the way, two to ward off dogs, one dangles after, always rather dirty. What am I?")
    while counter>7 and counter<11:
        answerList = ["cow", "a cow", "cows", ]
        stringI = input("Type your guess: ")
        if stringI.lower() in answerList:
            counter = 12
        else:
            print("\nNope! Try again! You have "+str(counter-8)+" guesses left for this riddle!\n")
            counter = counter-1
            if counter == 7:
                print("combat")
