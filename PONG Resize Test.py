import pygame
from pygame.locals import * 

pygame.init()

# Define colors/ honestly dont think I have to do this but I do anyways 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Creating the window
pygame.display.set_caption("PONG")

window_size = window_width, window_height = 950, 540
window = pygame.display.set_mode ((window_size), pygame.RESIZABLE) #---------> should allow a drag feature

#Main part of code includes: midline, updating color fill 
running = True

clock = pygame.time.Clock() 

while running:

        pygame.time.delay(100) #milliseconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False

            if event.type == VIDEORESIZE:
                window = pygame.display.set_mode ((event.w, event.h), pygame.RESIZABLE)

#-----------PUT OBJECTS ETC IN HERE-----------------
        #Making the fill in color black for window resizing/once again I think the default colors are black and white  
        window.fill(BLACK)

        #drawing the middle line ---------> need to get this to update based on x,y values only 
        pygame.draw.line(window, WHITE, [475, 0], [475, 540], 5)
        #updating the display
        pygame.display.flip() 

        clock.tick(60) #60 FPS
        
#Ends the program/event
pygame.quit()
            
        
