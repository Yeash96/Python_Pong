# This is Khrystarlite's signature hugging rabbit.
print(" () ()")
print("<('w')>")

# This scratch file contains the main loop that initializes pygame and used the modules to run the game.


# Python packages
import pygame               # Python game creation framework - the main backend.
import asyncio, sys                  

from modules import Network, Player  # Player module for the pong paddles.



def redrawWindow(window):
    window.fill(pygame.Color(0,0,0))
    player_Group.draw(window)
    # Draws the player sprites to the display window
    # Updates the display window whenever the sprites update
    pygame.display.update()
    # Updates the window so that areas where sprites were previouslyu return to the display window's background color.
    # Limits FPS to 60
    # print(p2.rect.right)



# The main loop.
def main():
    n = Network()

    # Create static variables:
    fps = 60                    # The standard frames per second - limited so that the game does not automatically 
                                #   use all system resources.
    p_Speed = 12                # The current speed the player paddles move at.
    win_W, win_H = 960, 540     # Dimensions for the current game window.
    clock = pygame.time.Clock() # Used with fps variable to limit the fps of the game.


    # Initialize pygame and its assets so they can be used
    pygame.init() 
    
    start.Pos = n.getPos()

    # Create player objects for the paddles.
    p = Player(1, boardDim=(win_W, win_H))

    # create an object that represents the display window.
    window = pygame.display.set_mode( (win_W, win_H) )

    # Test window title.
    pygame.display.set_caption( "Client Player Test" ) 
    
    # Create a group of sprites that will update with inputs and display movement
    player_Group = pygame.sprite.Group()  
    player_Group.add(p1)
    player_Group.add(p2)

    # The main game loop. Runs until the exit button is clicked. May add exit function within main menu.
    while True:
        clock.tick(fps)


        # Checks if the game is exited.
        for event in pygame.event.get():
            if event.type == pygame.QUIT : 
                pygame.quit()
                sys.exit()

        # pygame will listen for keyboard inputs.
        #   May be moved to player class later
        pressed = pygame.key.get_pressed()
        
        # V1 - Uses move - (v1)
        # Listens for the w and s keys to move Player 1.
        if pressed[pygame.K_w]:
            p1.move(-p_Speed)
        elif pressed[pygame.K_s]:
            p1.move(p_Speed)
        # Listens for the UP_arrow and DOWN_arrow keys to move Player 2.
        if pressed[pygame.K_UP]:
            p2.move(-p_Speed)
        elif pressed[pygame.K_DOWN]:
            p2.move(p_Speed)


        redrawWindow(window, player_Group)
        


        


# Runs the main function  when the program is run
if __name__ == '__main__':
    main()