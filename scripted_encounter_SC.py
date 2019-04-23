from GUI import *
import scripted_encounter_main

def scripted_encounter_runner():
SC = false
if SC == false:
    print("Pacing the front of the room is someone who must be your science teacher, Mr. Pitters, but he's now 1 foot shorter, covered in green skin, and has a scrunched up, rat-like face. In his hands are vials full of frothing, exotically colored liquids. He looks at you, mania dancing in his eyes, his teeth bared in a hungry leer. 'Are you ready for your chemistry assignment?'\n")
    c1 = scripted_encounter_main.choice(["Okay", "No?", "You look unusally good today Mr. Pitters.", "What are you supposed to be?"])
    SC = true
    if c1==0:
        print("\nExcellent!\n" )
    elif c1==1:
        print("\nToo bad, you're here now.\n")
    elif c1==2:
        print("\nI'll let that one slide, since today's assignment must be quite nerve wracking for students of your caliber.")
    elif c1==3:
        print("\nLost your memory? Hope you haven't forgotten your chemicals! I'm Mr. Pitters, your favorite chemistry teacher!")
        c1 = scripted_encounter_main.choice(["Whatever", "Sure!"])

    print("Your assignment is simple, make something in the lab that I'll remember for the rest of my life, something truly special. You have until school's out. With that, Mr. Pitters sits back at his desk.\n\nYou go to the nearest desk with a tray of full beakers, the top of it covered with pencil scratches, and some paper and a crucifix necklace stuffed in the table's innards.\n\nThe following chemicals are on your desk: Acetic Acid, Sodium Chloride, Dihydrogen Monoxide, Sodium Oxide, Ethanol, Felix Felocide, Ammonium Hydroxide, Ether, Sulfuric Acid.")
    solve = false
    while (solve = false):
        lab = scripted_encounter_main.choice(["Acetic Acid", "Sodium Chloride", "Dihydrogen Monoxide", "Sodium Oxide", "Ethanol", "Felix Felocide", "Ammonium Hydroxide", "Ether", "Sulfuric Acid\n\n"])
        counter = 0
        if counter>0:
            lab = scripted_encounter_main.choice(["Acetic Acid", "Sodium Chloride", "Dihydrogen Monoxide", "Sodium Oxide", "Ethanol", "Felix Felocide", "Ammonium Hydroxide", "Ether", "Sulfuric Acid, Show Mr. Pitters\n\n"])
            if lab==1:
                counter = counter+1000
                if(counter<1000 and counter=0):
                    print("The salt hits the bottom of the container.\n")
                elif(counter<1000 and counter!=0):
                    print("The salt floats to the bottom of the container.\n")
                elif(counter=2000):
                    print("The salt dissolves into the water, and the crucifix begins to emit a dim glow in the desk.")
                    lab2 = scripted_encounter_main.choice(["Investigate Crucifix Necklace\n\n"])
                    if(lab2==1):
                        print("You grab the necklace and bring and as your hand moves near your mixture, the liquid glows and becomes a shade of deadly gold, it's difficult to hold on to the container, a dull pain manifesting when you hold the container.")
                elif(counter<2000):
                    print("The salt dissolves into the mixture, and the crucifix necklace seems to shine, but dims just as quick. Was it a trick of the light?")
            elif lab==2
                counter = counter+1000
                if(counter<1000 and counter=0):
                    print("The water flows into the empty container.\n")
                elif(counter<1000 and counter!=0):
                    print("The water mixes in with the other substances, making small clouds in the mixture.\n")
                elif(counter=2000):
                    print("The salt dissolves into the water, and the crucifix begins to emit a dim glow in the desk.\n")
                    lab2 = scripted_encounter_main.choice(["Investigate Crucifix Necklace\n\n"])
                    if(lab2==1):
                        print("You grab the necklace and bring and as your hand moves near your mixture, the liquid glows and becomes a shade of deadly gold, it's difficult to hold on to the container, a dull pain manifesting when you hold the container.")
                elif(counter<2000):
                    print("The salt dissolves into the mixture, and the crucifix necklace seems to shine, but dims just as quick. Was it a trick of the light?")

            elif lab==7
                print("You bring the container to Mr. Pitters.")
                if(counter=2000)
                    s = scripted_encounter_main.choice(["Give it to Mr. Pitters, Throw it at Mr. Pitters\n\n"])
                    if(s==1):
                        print("Mr. Pitters takes a swig of the liquid. He then smacks his lips and is about to say something when his body begins to slowly dissolve into golden ash.")
                        solve = true
                    elif(s==2):
                        print("Throwing the golden liquid, you see that Mr. Pitter's shocked expression quickly changes to one of agony, as his body begins dissolving into golden ash.")
                        solve = true
                else
                    s = scripted_encounter_main.choice(["Give it to Mr. Pitters\n\n"])
                    if(s==1):
                        print("Mr. Pitters takes a swig of the liquid. He then smacks his lips before speaking. 'Nope, try again.' You make your way back to your table.")

            else:
                x = randomint(1, 5)
                if(x==1)
                    print("The mixture shows little sign of activity.\n" )
                if(x=2)
                    print("The mixture seems to slowly change color and odor.")
                if(x=3)
                    print("The mixture seems changes color in an instant, and the liquid loses its odor.")
                if(x=4)
                    print("The mixture becomes clear, but smells like rotten eggs.")
                if(x=5)
                    print("The mixture changes into a delicate shade of puke green.")
