from GUI import *
import scripted_encounter_main

def scripted_encounter_runner():


    if scripted_encounter_main.HI == 0:
        output("At the front of the dusty room, is your history teacher, old, sundried Mr. Williams. Funnily enough, Mr. Williams and the history classroom look entirely like they used to, apart from the lack of students.\nWhatever happened to the school either somehow missed him, or felt Mr. Williams didn't need any changing.\nOne thing that is odd is that the small national flag atop Mr. William's desk has a different flag on it instead. \n\nAs you enter the room, Mr. Williams's head turns slowly to look at you\n'Your late, find a seat.'")
        c1 = scripted_encounter_main.choice(["*take a seat*", "Whatever", "*turn to leave*", "What's with the new flag?"])
        scripted_encounter_main.HI = 1
        if c1==0:
            output("\n" )
        elif c1==1:
            output("\nHe just stares unblinkingly at you, like he's distracted\n")
        elif c1==2:
            output("\nThe door out slams shut of its own accord, and Mr. Wiliams just stares unblinkingly at you, like he's distracted\n")
        elif c1==3:
            output("\nHe just stares unblinkingly at you, like he's distracted\n")

        output("Mr. Williams's head slowly tracks you with his gaze as you sit at a desk, but as you turn back to face him, your eye catches certain oddities as you process the new scene, mainly that there are multiple Mr. Williams in the room, their images overlapping like bad interference.\nIn unison, the Williamses pass out papers on each desk.\nThe distorted Williamses, whose face is now too chaotic to look at without hurting, silently puts a paper on your desk.\nAs you reach out for the paper, you notice it is also distorted much the same way your teacher is.\nInstructions are found at the top of the page.\n'This is a 6 question pop quiz covering years 1900-1950, touching mainly upon the German sucess during the First Welktrieg and its decline in the Second Welktrieg.")


        counter = 0

        output("Q1. Whose assassination triggered the First WeltKrieg, also known as the First World War?\n")
        q1 = scripted_encounter_main.choice(["Archduke Ferdinand", "Kaiser Wilhelm II", "Leon Trotsky", "Winston Churchill"])
        if q1==0:
            output("\n" )
            counter = counter+1
        elif q1==1:
            output("\n" )
        elif q1==2:
            output("\n" )
        elif q1==3:
            output("\n" )
        output("Q2. What was the name of the peace treaty signed by the remainder of the Entente and the Central Powers at the end of the First Weltkrieg?\n")
        q2 = scripted_encounter_main.choice(["The Lasting Peace", "Peace with Hope", "Peace with Honour", "The Berlin Accord"])
        if q2==0:
            output("\n" )
        elif q2==1:
            output("\n" )
        elif q2==2:
            output("\n" )
            counter = counter+1
        elif q2==3:
                output("\n" )
        output("Q3. Where did the British Royalty flee to following the 1925 British Workers Uprising?")
        q3 = scripted_encounter_main.choice(["The Dominion of India", "The Dominion of Canada", "The Australasian Commonwealth", "The West Indies Confederation\n"])
        if q3==0:
            output("\n" )
        elif q3==1:
            output("\n" )
            counter = counter+1
        elif q3==2:
            output("\n" )
        elif q3==3:
            output("\n" )
        output("Q4. Who won the Second America Civil War?")
        q4 = scripted_encounter_main.choice(["The United States of America, under the military junta of General MacArthur", "The American Union State, led by Huey Long", "The Combined Syndicates of America, led by Chairman Reed", "The Pacific States of America, led by Hiram Johnson\n"])
        if q4==0:
            output("\n" )
            counter = counter+1
        elif q4==1:
            output("\n" )
        elif q4==2:
            output("\n" )
        elif q4==3:
            output("\n" )
        output("Q5. Which revolutionary leftist ideology grew in popularity following the German success in the First Weltkrieg?\n")
        q5 = scripted_encounter_main.choice(["Communism", "Socialism", "Anarchism", "Syndicalism\n"])
        if q5==0:
            output("\n" )
        elif q5==1:
            output("\n" )
        elif q5==2:
            output("\n" )
        elif q5==3:
            output("\n" )
            counter = counter+1
        output("Q6. Which nation's islands did the exiled British royalty occupy to facilitate their invasion of Great Britain?\n")
        q6 = scripted_encounter_main.choice(["Denmark", "Finland", "The West African Commune", "Netherlands"])
        if q6==0:
            output("\n" )
            counter = counter+1
        elif q6==1:
            output("\n" )
        elif q6==2:
            output("\n" )
        elif q6==3:
            output("\n" )
        output("Q7. What is the name of the Indian revolutionary which allowed the Bharatiya Commune from East India to annex the rest of the Indian subcontinent?\n")
        q7 = scripted_encounter_main.choice(["Mahatma Gandhi", "Lakshmi Sahgal", "Subhas Chandra Bose", "Lala Lajpat Rai"])
        if q7==0:
            output("\n" )
        elif q7==1:
            output("\n" )
        elif q7==2:
            output("\n" )
            counter = counter+1
        elif q7==3:
            output("\n" )
        output("Q8. Which of the following famous landmarks were destroyed in the Second Weltkrieg?\n")
        q8 = scripted_encounter_main.choice(["Taj Mahal", "The Eiffel Tower", "Brandenburg Gate", "Washington Monument"])
        if q8==0:
            output("\n" )
        elif q8==1:
            output("\n" )
            counter = counter+1
        elif q8==2:
            output("\n" )
        elif q8==3:
            output("\n" )
        output("Q9. Which of these German colonies fell to native rebellion?\n")
        q9 = scripted_encounter_main.choice(["German Indochina", "German Mittelafrika", "German Mauritius", "German East Asia"])
        if q9==0:
            output("\n" )
            counter = counter+1
        elif q9==1:
            output("\n" )
        elif q9==2:
            output("\n" )
        elif q9==3:
            output("\n" )
        output("Q10. Which of the following nations started the Second Weltkrieg by declaring war on the German Empire?\n")
        q10 = scripted_encounter_main.choice(["French Commune", "Union of Britain", "The United States", "The Socialist Republic of Italy"])
        if q10==0:
            output("\n" )
            counter = counter+1
        elif q10==1:
            output("\n" )
        elif q10==2:
            output("\n" )
        elif q10==3:
                output("\n" )
