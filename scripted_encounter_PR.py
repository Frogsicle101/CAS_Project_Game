from GUI import *
import scripted_encounter_main

def scripted_encounter_runner():

    if PR == false:
        print("You exit the portal, and find yourself in the high school office. Administraots walk to and fro, the padding of shoes and click-clack of heels can be heard, but it's aimless and discordant. One of the secretaries looks up from her work, and points at a door on the far end of the office with her pen. 'He's waiting.'\n")
        c1 = scripted_encounter_main.choice(["Who is?", "Is it too late to reschedule?", "What does he want?"])
        PR = true
        if c1==0:
            print("\n'The principal. Now go.'\n" )
        elif c1==1:
            print("\n'The principal hates rescheduling, and he's been expecting you, best not keep him waiting.'\n")
        elif c1==2:
            print("\n'That's between you and the principal, and the easiest way to find out is through that door.'")

        print("You make your way into the principal's office, and you are greeted with the sight of your principal, his face contorted in a macabre smile, his fangs visible.\n'It's about time you showed up. We're not like the others here.'\nHe nods his head toward the door.\n'Our kind needs to stick together' He takes a sip from his coffee mug, and you notice the crimson red of the liquid.")
        c2 = scripted_encounter_main.choice(["And do what, exactly?", "I'm not sure I like where this is going...", "Go on."])
        if c2==0:
            print("\n'Dominate. I wished yesterday to be powerful, and the entity that listened gave me this. It has given you this power too, why not work together and rule this little kingdom of ours?'\n" )
        elif c2==1:
            print("\nYou and I, we've been changed, molded to dominate over others. I wished yesterday to be powerful, and the entity that listened gave me this. It has given you this power too, why not work together and rule this little kingdom of ours?'\n")
        elif c2==2:
            print("\nYou and I, we've been changed, molded to dominate over others. I wished yesterday to be powerful, and the entity that listened gave me this. It has given you this power too, why not work together and rule this little kingdom of ours?'\n")
        c2 = scripted_encounter_main.choice(["And do what, exactly?", "I'm not sure I like where this is going...", "Go on."])
        if c2==0:
            print("\n'Dominate. I wished yesterday to be powerful, and the entity that listened gave me this. It has given you this power too, why not work together and rule this little kingdom of ours?'\n" )
        elif c2==1:
            print("\nYou and I, we've been changed, molded to dominate over others. I wished yesterday to be powerful, and the entity that listened gave me this. It has given you this power too, why not work together and rule this little kingdom of ours?'\n")
        elif c2==2:
            print("\nYou and I, we've been changed, molded to dominate over others. I wished yesterday to be powerful, and the entity that listened gave me this. It has given you this power too, why not work together and rule this little kingdom of ours?'\n")
