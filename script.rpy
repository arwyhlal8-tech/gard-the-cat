# Déclaration des images redimensionnées (1920x1080)
image bg madcal = Transform("madcal", xysize=(1920, 1080))
image bg ckitchen = Transform("ckitchen", xysize=(1920, 1080))
image bg babe = Transform("babe", xysize=(1920, 1080))
image bg tri9 = Transform("tri9", xysize=(1920, 1080))

# Declare characters used by this game.
define e = Character("Eileen")
define m = Character("[player_name]", color=("#FFFA83"))
define A = Character("Arwa", color=("#A4D6FF"))

# The game starts here.

label start:

    # Demande le nom du joueur
    $ player_name = renpy.input("What is your name?", default="")
    $ player_name = player_name.strip()
    
    if player_name == "":
        $ player_name = "Meow"
        
    scene bg madcal
    with dissolve

    show cat at center
    "Here I am, standing in the middle of this quiet house."
    "I look down at the small black cat sitting right in front of me."
    "I think this is the cat I have to guard for the next few days."
    "It's so cute, staring at me with those big, curious eyes!"
    "Let's see around... Oh, the boss left a note on the table for her caretaker."
    
    menu:
        "See the note":
            jump seethenote

        "Ignore the note":
            jump egnor   

label seethenote:
    scene bg ckitchen
    with fade
    show note1 at center
   
    "I pick up the pink note and read the instructions carefully."
    "Alright, now I have to give the cat its special food and clean the litter box."
    "The note also says I need to keep an eye on the windows and check the doors."
    "And after that, I'll definitely look around for any other hidden notes."
    
    scene bg ckitchen
    show cat at center   
    m "Wino wino, cute cute Lily!"
    m "Come here my little princess, it's time to feed you."
    "I pour the food into her bowl. There it is, she's eating happily."
    "Watching her eat brings a warm smile to my face. Such a peaceful moment."
    
    menu:
        "Clean the box":
            jump clene

        "Explore the hallway":
            jump explore_hallway

        "Go to sleep":
            jump sleep 

label explore_hallway:
    scene bg madcal
    with dissolve
    "I decide to walk around the house before doing anything else."
    "The corridors are long and a bit chilly. Dust particles float in the dim light."
    "I hear a strange scratching sound coming from the living room corner..."
    "Is someone—or something—outside the window?"
    "My heart beats a little faster. I should probably focus on the chores listed in the note first."
    
    menu:
        "Clean the box":
            jump clene

        "Go to sleep":
            jump sleep

label clene:
    scene bg babe
    with fade
    "I walk over to the corner where the litter box is kept."
    "That's it... ugh, it's sooo messy and smells bad, but okay, someone has got to do it."
    "I hold my breath, clean it up as fast as I can, and wash my hands."
    "Alright, the chore is finally done. What now?"
    
    menu:
        "See the other note":
            jump othernot

        "Check the front door":
            jump check_door

        "Go to sleep":  
            jump gotosleep

        "Nothing": 
            jump nothing

label check_door:
    scene bg babe
    with dissolve
    "I walk cautiously toward the heavy front door to make sure it's safely locked."
    "I twist the lock twice. Good, it's secure."
    "Suddenly, my phone buzzes in my pocket with a strange notification."
    "It's an email alert reminding me about the house rules and security protocols."
    "Glad I checked the door just in time!"
    
    menu:
        "See the other note":
            jump othernot

        "Go to sleep":
            jump gotosleep

        "Nothing": 
            jump nothing

label othernot:    
    scene bg ckitchen
    with fade
    show note2 at center
    "I spot a second note resting near the kitchen counter."
    "It says: 'So we need to play with the cat, make sure to take the Gmail security update, and also eat dinner.'"
    "I follow every single step carefully."
    "Okay, now I played with the cat with a toy string, took the Gmail security code, and ate a quick snack. Tout bien !"
    "Everything is in order. Now we can finally choose to sleep."
    "Finally, I'm so tired after a long day of guarding this mysterious house."
    
    scene bg ckitchen
    with fade
    A "Hi! You finished the game, that's a good ending. Thanks for playing!"
    return

label nothing:
    scene bg ckitchen
    with fade
    show arwa at center
    A "Oh hi! My name is Arwa Hilal, the developer of this game. I want to talk about myself."
    A "First, I am 15 years old, I'm from Morocco, and I speak Arabic and can communicate in English and French."
    A "I love math and physics, and I'm a good public speaker. I draw, I love reading, and I'm a graphic designer!"
    A "This is my 4th game, so I hope you're interested in seeing my other games. Thank you!"
    A "If you want to say anything to me, here is my Gmail, I will reply: arwyhlal8@gmail.com. Bye!"
    A "Try again and thanks for playing my game!"
    A "And the idea is inspired by the Roblox game named 7 Day Cat."
    A "MWAH and I love all of you :>"
    return

label egnor:
    scene bg ckitchen
    with fade
    "I decide to completely ignore the note left by the boss."
    "I'll just feed the cat quickly, clean the box, and grab something to eat for myself."
    "So now we fed the cat, cleaned the box, and ate. I'll also close the window and the curtains just in case."
    "Now let's go straight to sleep without checking anything else."
    
    scene bg tri9
    with dissolve
    A "Oops, you didn't take the Gmail security instructions, that's bad. Try again!"
    return

label sleep:
    scene bg ckitchen
    with fade
    A "Oh, you died! You didn't feed or take care of yourself properly, that's bad. Try again and be careful!" 
    return

label gotosleep:
    scene bg ckitchen
    with fade
    A "Oh, you died, baby. You went to sleep leaving the front door completely unlocked and unattended. Try again, baby!"
    return

label sleepbeforsheck:
    scene bg ckitchen
    with fade
    show wa7che at center
    A "Oh, you died! You left someone or something inside the house."
    A "Try . again!"
    return