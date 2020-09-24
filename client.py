# This is Khrystarlite's signature hugging rabbit.
print(" () ()")
print("<('w')>")

# This scratch file contains the main loop that initializes pygame and used the modules to run the game.


# Python packages
import pygame               # Python game creation framework - the main backend.
import sys                  

from modules import Network, Player2, Spectator  # Player module for the pong paddles.

# Create static variables:
fps = 60                    # The standard frames per second - limited so that the game does not automatically 
                            #   use all system resources.
p_Speed = 12                # The current speed the player paddles move at.
win_W, win_H = 960, 540     # Dimensions for the current game window.

# Initialize pygame and its assets so they can be used
pygame.init() 

def read_Pos(string: str):
    # print(string)
    string = string.split(",")
    return int(string[0]), int(string[1])
def make_pos(pos: tuple):
    return str(pos[0]) + "," + str(pos[1])



# def redrawWindow(window, p, op):
def redrawWindow(window, player_Group):
    window.fill(pygame.Color(0,0,0))
    # p.draw(window)
    # op.draw(window)
    player_Group.draw(window)
    pygame.display.update()



# The main loop.
def main():
    n = Network()
    # print(n.server)
    clock = pygame.time.Clock() # Used with fps variable to limit the fps of the game.
    player_Pos = n.getPos()
    player = Player2(read_Pos(player_Pos))
    # opponent =P
    # player = (p)
    # p_num = p_and_Pos[0]
    # print("Player", p_Num)

    

    
    

    

    # # Create static variables:
    # fps = 60                    # The standard frames per second - limited so that the game does not automatically 
    #                             #   use all system resources.
    # p_Speed = 12                # The current speed the player paddles move at.
    # win_W, win_H = 960, 540     # Dimensions for the current game window.

    print("tmp Done")
    

    # # Create player objects for the paddles.
    # # TODO: write a way to create opponet
    # if p_Num <= 1:
    #     p = Player2(p_Num, boardDim=(win_W, win_H))
    #     # op = Player2
    # else:
    #     p = Spectator(p_Num)

    # # create an object that represents the display window.
    # window = pygame.display.set_mode( (win_W, win_H) )

    # # Test window title.
    # pygame.display.set_caption( "Client Player Test" ) 
    
    # # Create a group of sprites that will update with inputs and display movement
    # player_Group = pygame.sprite.Group()  
    # # player_Group.add(p1)
    # # player_Group.add(p2)
    # player_Group.add(p)
    # player_Group.add(op)

    # # The main game loop. Runs until the exit button is clicked. May add exit function within main menu.
    while True:
        clock.tick(fps)

        opPos = read_Pos(n.send(make_pos((player.rect.centerx,player.rect.centery)) ))
    #     # op.rect.centerx,opPos.rect.centery = opPos
    #     op.rect.y = opPos[1]


    #     # Checks if the game is exited.
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT : 
    #             pygame.quit()
    #             sys.exit()

    #     # pygame will listen for keyboard inputs.
    #     #   May be moved to player class later
    #     pressed = pygame.key.get_pressed()
        
    #     # V1 - Uses move - (v1)
    #     # Listens for the w and s keys to move Player 1.
    #     if pressed[pygame.K_w]:
    #         p1.move(-p_Speed)
    #     elif pressed[pygame.K_s]:
    #         p1.move(p_Speed)
    #     # Listens for the UP_arrow and DOWN_arrow keys to move Player 2.
    #     if pressed[pygame.K_UP]:
    #         p2.move(-p_Speed)
    #     elif pressed[pygame.K_DOWN]:
    #         p2.move(p_Speed)


    #     redrawWindow(window, player_Group)
        


        


# Runs the main function  when the program is run
if __name__ == '__main__':
    main()