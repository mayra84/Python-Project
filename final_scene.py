from pygame import mixer
import os
import time

def final_scene():
    
    input('')
    mixer.init()
    mixer.music.load("./sounds/Sauron (Mordor) Theme - Lord of the Rings _ EPIC VERSION.wav")
    mixer.music.play()
    os.system('clear')

    input("""
Chapter 4: The Final Scene
***  *   *  ** **    **   *  **  *  * * 
   *  *          **    * *        ** * *
    *      *       **       *   *       
  *     *                             * 
                    *                   
*   *      *     *          *   *      *
                                   *    
  
""")


    input('\nThere it is. Mount Doom. Finally.🌋\n')

    input('\nAfter all the obstacles and friends lost along the way, Sam and Frodo arrive at Mount Doom.\n ')

    input('\nFrodo\'s body fails him.\n')

    input("""\"I cannot go on, Sam. All I can see is the Eye of Sauron. There's nothing, no veil between me and the wheel of fire. I can see him with my waking eyes!\"""")
    
    input("""\n\"Then let us be rid of it once and for all! Come on Mr. Frodo, I can't carry it for you, but I can carry you!\" """)

    input('\nSam picks Frodo up and puts him across his shoulder he staggers forward, gets his balance and begins to move up the mountain step by step.\n')

    while True:
        user_choice_5 = input("""
    What happens next: 
    1 - Frodo and Sam make it to the heart of the mountain, with no interruption. They stand at the edge of the fires and are finally ready to end their tired quest. 
    2 - Frodo and Sam are close to the door of Mount Doom when Smeagol, a creature obsessed with the One Ring, attacks them and threatens to take the Ring for himself.
    q- You quit and forsake the peoples of Middle-Earth.
    :""")
        choice_options = ['1', '2','q']
        if user_choice_5 not in choice_options:
            print('\nThat is not a valid option. Please try again.')
            False
        elif user_choice_5== '1':
            input('\nAt the edge of fulfilling his quest, Frodo finally yields to the will of the One Ring.\n') 
            
            input('\nHe is influenced by its evil to return the ring to Sauron.👹💍 Mission failed. Everyone dies. RIP.🪦\n')
            mixer.music.load("./sounds/Fail - sound effect.wav")
            mixer.music.play() 
            break

        elif user_choice_5 == '2':
            input('\nA fight with Smeagol ensues and Sam is able to hold him back while Frodo makes it to the heart of Mount Doom.\n') 
            
            input('\nAt the edge of fulfilling his quest, Frodo finally yields to the will of the One Ring and puts it on his finger, betraying the quest.\n')

            input('\nBut Smeagol knocks out Sam and charges at Frodo!\n')

            mixer.music.fadeout(4000)
            
            input('\nSmeagol manages to bite off Frodo\'s finger which held the Ring.\n')

            input('\nThey begin to fight for the Ring and Smeagol falls into the fires of Mount Doom along with The One Ring to Rule Them All.\n')

            time.sleep(3)

            print('\n\n\nSauron and The One Ring are finally destroyed.\n\n\n')
            


            mixer.init()
            mixer.music.load("./sounds/The Shire.wav")
            mixer.music.play()
            time.sleep(5)
            os.system('clear')
            
            print("""


* ** * *   *  **  *  *   **   *   * *  **  ****  *   ** *   *      **   **   ** **   *   *  ** *   *   **    *  * * *   * *    **       ** ** *   * * *     ** 
        * *                  * **    *          *  **  * *   ***       *  *       ***             * **      *  * * *     *  **   *  * *   *  *   * * *   ***  *
    *    *   *  *  *  * *   *      *  *  *                *     * *  *      *         **  *   *  *       **          **       *  * *                    *      
   *           *              *         *               *           *            *       *   *     *   *                *                *  *    *             
                      *     *                                  **      *           *  **    *    *        *    *     **            *                       *   
             *  *  *    *      **                             *   *  *      *             *    *    **  **                  *   *            *    * * * * *    
         * *                 *         *   *  *      *                          *                 *               *       *                *                   
    **    *               *       ***       **         *                **    *     **                           * **    *    **    *     *     *            **
       **                                       ** *        **                                              **               *                *          *     
                                                                          *                                                             *                      
  *           *          *            *  *                *        *         *                **                                *  *            * * * *        
*                 *  *               *              * *  *                        *                             *                                  * *      *  


I have found that it is the small everyday deed of ordinary folks that keep the darkness at bay. Small acts of kindness and love." \n - Gandalf (J.R.R. Tolkien)


* ** * *   *  **  *  *   **   *   * *  **  ****  *   ** *   *      **   **   ** **   *   *  ** *   *   **    *  * * *   * *    **       ** ** *   * * *     ** 
        * *                  * **    *          *  **  * *   ***       *  *       ***             * **      *  * * *     *  **   *  * *   *  *   * * *   ***  *
    *    *   *  *  *  * *   *      *  *  *                *     * *  *      *         **  *   *  *       **          **       *  * *                    *      
   *           *              *         *               *           *            *       *   *     *   *                *                *  *    *             
                      *     *                                  **      *           *  **    *    *        *    *     **            *                       *   
             *  *  *    *      **                             *   *  *      *             *    *    **  **                  *   *            *    * * * * *    
         * *                 *         *   *  *      *                          *                 *               *       *                *                   
    **    *               *       ***       **         *                **    *     **                           * **    *    **    *     *     *            **
       **                                       ** *        **                                              **               *                *          *     
                                                                          *                                                             *                      
  *           *          *            *  *                *        *         *                **                                *  *            * * * *        
*                 *  *               *              * *  *                        *                             *                                  * *      *  




""")
            
            # input('\n\n\n\n"I have found that it is the small everyday deed of ordinary folks that keep the darkness at bay. Small acts of kindness and love." \n - Gandalf (J.R.R. Tolkien\n\n\n\n')
            
            
            
            time.sleep(8)
            break
        elif user_choice_5 == 'q':
            print('\nSauron thanks you.\n')
            exit()

# final_scene()