from pygame import mixer 
import os 
from gandalf_vs_balrog import gandalf_vs_balrog

def the_fellowship_of_the_terminal():

    mixer.init()
    mixer.music.load("./sounds/The Lord of the Rings - Soundtrack - Main theme.wav")
    mixer.music.play()
    
    os.system('clear')

    input("""
Chapter 1: The Fellowship of the Terminal
***  *   *  ** **    **   *  **  *  * * 
   *  *          **    * *        ** * *
    *      *       **       *   *       
  *     *                             * 
                    *                   
*   *      *     *          *   *      *
                                   *    
  
""")
    

    input('\nFrodo Baggins🧑🏻‍🦱, Samwise Gamgee👦🏼, Merry Brandybuck🧑🏼‍🌾, and Pippin Took🧑🏼‍🌾, come across Aragorn🧔🏻‍♀️ in a tavern and he escorts the hobbits to Rivendell, an Elvish sanctuary.')
    
    input('\nElrond🧝🏽 holds a council of Elves, Men, and Dwarves, also attended by Frodo and Gandalf, that decides the Ring💍 must be destroyed in the fires of Mount Doom🌋.')

    input('\nFrodo🧑🏻‍🦱 volunteers to take the Ring to be destroyed!')

    

    while True: 
        mixer.music.fadeout(6000)
        user_choice_2 = input("""
    What happens next: 
    1 - Frodo is ignored and the council continues to deliberate the fate of the Ring... 
    2 - The council accepts Frodo's proposal and the Fellowship of the Ring is formed.
    q- You quit and forsake the peoples of Middle-Earth.
    :""")
        choice_options = ['1', '2','q']
        if user_choice_2 not in choice_options:
            print('\nThat is not a valid option. Please try again.\n')
            False 
        if user_choice_2 == '1':
            mixer.music.load("./sounds/Fail - sound effect.wav")
            mixer.music.play()

            print('\n\nBoromir of Gondor draws his sword which initiates a full-on battle and everyone dies. RIP.🪦\n') 
            input('')
            break
        elif user_choice_2 == '2':
            print("""
Take these, it's dangerous to go out there alone:
🧔🏻‍♀️🧝🏻‍♂️🧙🏻‍♂️🧑🏻‍🦱👦🏼🧑🏼‍🌾🧑🏼‍🌾🧔🏼👨🏾‍🚒
""")
            
            gandalf_vs_balrog()
            break
        elif user_choice_2 == 'q':
            print('\nSauron thanks you.\n')
            exit()
        

# the_fellowship_of_the_terminal()