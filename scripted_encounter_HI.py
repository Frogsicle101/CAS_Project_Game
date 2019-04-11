import scripted_encounter_main
ER = false
if ER == false:
    print("At the front of the dusty room, is your history teacher, old, sundried Mr. Williams. Funnily enough, Mr. Williams and the history classroom look entirely like they used to, apart from the lack of students.\nWhatever happened to the school either somehow missed him, or felt Mr. Williams didn't need any changing.\nOne thing that is odd is that the small national flag atop Mr. William's desk has a different flag on it instead. \n\nAs you enter the room, Mr. Williams's head turns slowly to look at you\n'Your late, find a seat.'")
    c1 = scripted_encounter_main.choice(["*take a seat*", "Whatever", "*turn to leave*", "What's with the new flag?"])
    ER = true
    if c1==0:
        print("\n" )
    elif c1==1:
        print("\nHe just stares unblinkingly at you, like he's distracted\n")
    elif c1==2:
        print("\nThe door out slams shut of its own accord, and Mr. Wiliams just stares unblinkingly at you, like he's distracted\n")
    elif c1==3:
        print("\nHe just stares unblinkingly at you, like he's distracted\n")

    print("Mr. Williams's head slowly tracks you with his gaze as you sit at a desk, but as you turn back to face him, your eye catches certain oddities as you process the new scene, mainly that there are multiple Mr. Williams in the room, their images overlapping like bad interference.\nIn unison, the Williamses pass out papers on each desk.\nThe distorted Williamses, whose face is now too chaotic to look at without hurting, silently puts a paper on your desk.\nAs you reach out for the paper, you notice it is also distorted much the same way your teacher is.\nInstructions are found at the top of the page.\n'This is a 6 question pop quiz covering years 1900-1950, touching mainly upon the German sucess during the First Welktrieg and its decline in the Second Welktrieg.)


    counter = 0

    print(Q1. Whose assassination triggered the First Weltkrieg?\n")
    while counter>-1 and counter<3:
        q1 = scripted_encounter_main.choice(["Archduke Ferdinand", "Kaiser Wilhelm ", "*Leon Trotsky", "Winston Churchill"])
        if q1==0:
            print("\n" )
            counter = counter+1
        elif c1==1:
            print("\n" )
        elif c1==2:
            print("\n" )
        elif c1==3:
            print("\n" )
    print("Greek philisophy is where this next riddles comes from!\n\nThere is one father and twelve children;\nof these each Has twice thirty daughters of different appearance:\nSome are white to look at and the others black in turn;\nThey are immortal and yet they all fade away.\n")
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
