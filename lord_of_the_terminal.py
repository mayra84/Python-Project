from pygame import mixer
import os
from start import start

def intro():

    mixer.init()
    mixer.music.load("/Users/mayra./Downloads/The Fellowship Theme - Lord of the Rings _ EPIC VERSION.wav")
    mixer.music.play()
    # mixer.sound.set_volume()

    os.system('clear')
   
    input("""
  _______ _            _                   _          __   _   _            _______                  _             _ 
 |__   __| |          | |                 | |        / _| | | | |          |__   __|                (_)           | |
    | |  | |__   ___  | |     ___  _ __ __| |   ___ | |_  | |_| |__   ___     | | ___ _ __ _ __ ___  _ _ __   __ _| |
    | |  | '_ \ / _ \ | |    / _ \| '__/ _` |  / _ \|  _| | __| '_ \ / _ \    | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
    | |  | | | |  __/ | |___| (_) | | | (_| | | (_) | |   | |_| | | |  __/    | |  __/ |  | | | | | | | | | | (_| | |
    |_|  |_| |_|\___| |______\___/|_|  \__,_|  \___/|_|    \__|_| |_|\___|    |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|
                                                                                                                     
                                                                                                                     
""")
    next_1 = input('\nIt began with the forging of the Great Rings.')

    next_2 = input('\n\n3 were given to the Elves🧝🏻‍♀️, 7 to the Dwarf-Lords👨🏾‍🚒, and 9 rings were gifted to the race of Men🧔🏻‍♀️, who above all else desire power. \nWithin these rings was bound the strength and the will to govern each race. \n\nBut... ')

    next_3 = input('\n\nThey were all of them deceived, for another ring was made. Deep in the land of Mordor, in the Fires of Mount Doom🌋, the Dark Lord Sauron👹 forged a master ring, and into this ring he poured his cruelty, his malice and his will to dominate all life. \n\nOne ring to rule them all.💍')

    next_4 = input('\n\nAfter a battle of men joined with elves against Sauron, the enemy of the free peoples of Middle-Earth, was defeated. The Ring passed to Isildur🧔🏻‍♂️, who had this one chance to destroy evil forever..... \n\nIsildur🧔🏻‍♂️ and Elrond🧝🏽 are in Mount Doom🌋. Elrond prompts Isildur "Cast it into the fire! Destroy it!" Isildur responds,"No."\n\n')

    beginning()


def beginning():
    mixer.music.fadeout(6000)
    user_choice_1 = input("""
    What happens next:
        1 - Elrond stares at Isildur as he walks away with the ring...
        2 - Elrond tackles Isildur, takes the ring, and throws it into the fires of Mount Doom...
        q - You quit and forsake the peoples of Middle-Earth.
        :""")
        # print(user_choice_1)
    choice_options = ['1', '2','q']
    if user_choice_1 not in choice_options:
        print('\nThat is not a valid option. Please try again.\n')
        beginning()
    elif user_choice_1 == '1' or user_choice_1 == '2':
        start(user_choice_1)
    elif user_choice_1 == 'q':
        print('\nSauron thanks you.\n')
        exit()

#When other functions finish executing, code will resume executing here. 
    user_choice_1_a = input("""

Would you like to play again?
1 - Yes, please.
2 - No, thank you.
:
""")
    if user_choice_1_a == '1':
        os.system('clear')
        intro() 
    if user_choice_1_a == '2':
        exit()
        # user_choice_1 = beginning()
    # return user_choice_1

intro()