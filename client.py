# This is Khrystarlite's signature hugging rabbit.
print(" () ()")
print("<('w')>")

# This scratch file contains the main loop that initializes pygame and used the modules to run the game.


# Python packages
import pygame               # Python game creation framework - the main backend.
import sys                  

from modules import Network, Player2, Spectator  # Player module for the pong paddles.



#TODO Player number
# Create static variables:
fps = 60                    # The standard frames per second - limited so that the game does not automatically 
                            #   use all system resources.
p_Speed = 12                # The current speed the player paddles move at.
win_W, win_H = 960, 540     # Dimensions for the current game window.

win = pygame.display.set_mode((win_W,win_H))
pygame.display.set_caption("Player ",str(Pnum+1))

# Initialize pygame and its assets so they can be used
pygame.init() 


def read_Pos(string: str):
    print(string)
    string = string.split(",")
    return int(string[0]), int(string[1])
def make_pos(pos: tuple):
    return str(pos[0]) + "," + str(pos[1])


def read_Pos_Spec(string: str):
    string = string.split(",")

    return int(string[0]),int(string[1]),int(string[2]),int(string[3]),


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

    print ("Pnum: ", Pnum)

    if Pnum <= 1:
        player = Player2(read_Pos(player_Pos))
        opp = Player2()

        p_Group = pygame.sprite.Group() 
        p_Group.add(player)            
        p_Group.add(opp)            

        while True:
            clock.tick(fps)

            opp.rect.centerx, opp.rect.centery = read_Pos(n.send(make_pos((player.rect.centerx,player.rect.centery)) ))
            opp.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            player.move()
            redrawWindow(win,p_Group)
    else:
        p1 = Player2()
        p2 = Player2()

        p_Group = pygame.sprite.Group() 
        p_Group.add(p1)            
        p_Group.add(p2)    

        while True:
            clock.tick(fps)

            p1.rect.centerx, p1.rect.centery = n.getPosSpect()
            p2.rect.centerx, p2.rect.centery

            p1.update()
            p2.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            player.move()
            redrawWindow(win,p_Group)



    Pnum+=1



        
   

        


# Runs the main function  when the program is run
if __name__ == '__main__':
    main()