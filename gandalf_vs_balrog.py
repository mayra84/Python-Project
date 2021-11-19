from pygame import mixer
import os
from the_two_towers import the_two_towers

def gandalf_vs_balrog():

    input('')
    
    os.system('clear')

    input("""
Chapter 2: Gandalf vs Balrog
***  *   *  ** **    **   *  **  *  * * 
   *  *          **    * *        ** * *
    *      *       **       *   *       
  *     *                             * 
                    *                   
*   *      *     *          *   *      *
                                   *    
  
""")

    input('The Fellowship- composed of a wizard, two men, an elf, a dwarf, and four hobbits- decide to go to the Mines of Moria, Gimli\'s👨🏾‍🚒 relatives home.')

    mixer.init()
    mixer.music.load("./sounds/THE LORD OF THE RING - URUK HAI THEME.wav")
    mixer.music.play()

    input('\nEveryone makes it to the Mines of Moria only to discover a barren castle. They had been trapped and killed by Orcs.')  
    

    input('\nThey quietly try to make their way through the castle when... ') 

    input('\nThey encounter a cave troll!🐏👹🔥')

    input("""
Gandalf the Grey courageously confronts the Balrog!


\t\t\t\t\t🧙🏻‍♂️ ✨⚡️💥 \t\t👹
""")

    input('\n"YOU SHALL NOT PASS!" Gandalf declares.\n')

    input('\nWith that, the ground gapes open and swallows the Balrog, sending him to the fiery depths!🔥🔥🔥\n')

    input("""As they begin to walk away, the Balrog cracks its whip and grabs Gandalf by the leg, pulling Gandalf down!😧""")

    input("""\nGandalf is holding on to the edge and says, \"Fly, you fools!\"""")
    

    while True:
        user_choice_3 = input("""
    What happens next: 
    1 - They heed Gandalf's advice and run out of the castle, leaving him behind.
    2 - They run to Gandalf and successfully rescue him from falling to the fiery depths with Balrog!🔥🔥🔥
    q- You quit and forsake the peoples of Middle-Earth.
    :""")
        choice_options = ['1', '2','q']
        if user_choice_3 not in choice_options:
            print('\nThat is not a valid option. Please try again.')
            False
        elif user_choice_3== '1':
            print('\nThanks to Gandalf\'s selfless sacrifice, the rest of the Fellowship manages to escape and make it out of the castle.\n') 
            mixer.music.fadeout(6000)
            the_two_towers()
            break
        elif user_choice_3 == '2':
            print('\nEveryone makes it out of the castle safely! They make it to the river and attacked by a hoard of Uruk-hai!! Everyone dies. RIP.🪦🪦🪦🪦🪦🪦🪦🪦🪦\n')
            mixer.music.load("./sounds/Fail - sound effect.wav")
            mixer.music.play()
            input('')
            break
        elif user_choice_3 == 'q':
            print('\nSauron thanks you.\n')
            exit()

# gandalf_vs_balrog()
