import scripted_encounter_main
ER = 0
if ER = 0:
    print("Sitting behind a large, wooden desk with a rotting, wormy apple atop it, is your English teacher. Ms. Kassandra. But she looks...different. Where her legs once were, are the hind quarters of a lion. Sprouting from her back are wings like that of an eagle. Most odd though, is that she's wearing a sweater that doesn't age her appearance twenty years. 'Welcome to class! I hope you're ready to dive right back into classic literature!'")
    c1 = scripted_encounter_main.choice(["Whatever", "Sure!", "What..happned to you?", "What's wrong wtih everyone here?"])

if c1==0:
    print("Well that's not very polite!" )
elif c1==1:
    print("Excellent!")
elif c1==2:
    print("If you had paid attention in class recently, you'd know I am a sphinx, a creature out of the muths of Ancient Greece! Now, who is ready to dive back into the classics!?")
    c1 = scripted_encounter_main.choice(["Whatever", "Sure!"])

print("'Well, let's begin. Today's lesson will be a practical lesson on a common wlement in all mythology: riddles!'' Ms. Kassandra's cheerful tone switched to one of grim foreboding as she looks regretfully towards the skeletons sitting at the desks. 'I hope you try harder than your peers.'"")
