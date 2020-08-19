# This is Khrystarlite's signature hugging rabbit.
print(" () ()")
print("<('w')>")

# This scratch file contains the main loop that initializes pygame and used the modules to run the game.


# Python packages
import pygame               # Python game creation framework - the main backend.
import sys
# import asyncio                  

from modules import Player  # Player module for the pong paddles.


# The main loop.
async def main():
def main():

    # Create static variables:
    fps = 60                    # The standard frames per second - limited so that the game does not automatically 
                                #   use all system resources.
    p_Speed = 12                # The current speed the player paddles move at.
    win_W, win_H = 960, 540     # Dimensions for the current game window.
    clock = pygame.time.Clock() # Used with fps variable to limit the fps of the game.


    # Initialize pygame and its assets so they can be used
    pygame.init() 

    # Create player objects for the paddles.
    p1 = Player(1, boardDim=(win_W, win_H))
    p2 = Player(2, boardDim=(win_W, win_H))

    # create an object that represents the display window.
    window = pygame.display.set_mode( (win_W, win_H) )

    # Test window title.
    pygame.display.set_caption( "Player Test" ) 
    
    # Create a group of sprites that will update with inputs and display movement
    player_Group = pygame.sprite.Group()  
    player_Group.add(p1)
    player_Group.add(p2)

    # The main game loop. Runs until the exit button is clicked. May add exit function within main menu.
    while True:

        # Checks if the game is exited.
        for event in pygame.event.get():
            if event.type == pygame.QUIT : 
                pygame.quit()
                sys.exit()

        # pygame will listen for keyboard inputs.
        #   May be moved to player class later
        # pressed = pygame.key.get_pressed()

        p1.move()
        p2.move()

        
        
        # Draws the player sprites to the display window
        player_Group.draw(window)
        # p1.draw(window)
        # p2.draw(window)
        # Updates the display window whenever the sprites update
        pygame.display.update()
        # Updates the window so that areas where sprites were previouslyu return to the display window's background color.
        window.fill(pygame.Color(0,0,0))
        # Limits FPS to 60
        clock.tick(fps)
        # print(p2.rect.right)

        


# Runs the main function  when the program is run
if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    main()