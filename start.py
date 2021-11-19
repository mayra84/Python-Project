from pygame import mixer
import os
from the_fellowship_of_terminal import the_fellowship_of_the_terminal


def start(user_choice_1):
    
    if user_choice_1 == '1':
        input('\nGood going, Elrond.😒 Isildur keeps the ring, eventually loses it, and it finds its way to the hobbit, Frodo Baggins.🧑🏻‍🦱💍\n')
        the_fellowship_of_the_terminal()
    elif user_choice_1 == '2':
        mixer.init()
        mixer.music.load("/Users/mayra./Downloads/Kids cheering Yay! (Sound effect).wav")
        mixer.music.play() 
        
        input('\nGood job, Elrond! The ring is destroyed and Middle-Earth lives in peace and prosperity.🥳🤍✨\n')

    # input('')
    # os.system('clear') 
# start()