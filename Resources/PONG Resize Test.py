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
class Block(pygame.sprite.Sprite):

    
    def __init__( self, width, height ):
        super(Block,self ).__init__()
        #''' things needed to draw object below'''
        self.image = pygame.Surface( (width,height) ) 
        self.image.fill ( pygame.Color(0,0,255) )
        self.rect = self.image.get_rect()
        
    def Setpostion(self, x, y):
        self.rect.x = x
        self.rect.y = y
        
    def UpdateSize(self, width, height): #update surface
        self.image = pygame.Surface( (width, height ) )
        self.image.fill ( pygame.Color(0,0,255) )
        self.rect = self.image.get_rect()
     
     
border=pygame.sprite.Group()
topwall = Block( window_width, 10 )
topwall.Setpostion( 0, 0 )
bottomwall = Block( window_width,10 )
bottomwall.Setpostion( 0, window_height-10 )
leftwall = Block( 10, window_height )
leftwall.Setpostion(0,0)
rightwall = Block( 10, window_height)
rightwall.Setpostion( window_width-10, 0)
bounds = pygame.Rect( 10, 10, window_width-20, window_height-20 )
board =  Block( bounds.w , bounds.h)
board.Setpostion(10,10)
board.image.fill ( pygame.Color(0,255,0) )
border.add( topwall, bottomwall, leftwall, rightwall, board )
border.add( board)
border.draw( window )        

while running:

        pygame.time.delay(100) #milliseconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False

            if event.type == VIDEORESIZE:
                window = pygame.display.set_mode ((event.w, event.h), pygame.RESIZABLE)
                window_size = window_width, window_height = event.w, event.h 
                print(window_height)
                bounds = pygame.Rect( 10, 10, window_width-20, window_height-20 )
     
                board.UpdateSize( bounds.w, bounds.h )#u[date surface 
                board.Setpostion(10,10)
                
                topwall.UpdateSize( window_width, 10 )
                topwall.Setpostion( 0, 0 )
                bottomwall.UpdateSize( window_width, 10 )
                bottomwall.Setpostion( 0, window_height-10 )
                leftwall.UpdateSize( 10, window_height )
                leftwall.Setpostion( 0, 0 )
                rightwall.UpdateSize( 10, window_height )
                rightwall.Setpostion( window_width-10, 0 )                

                board.image.fill ( pygame.Color(0,255,0) )
                print(bounds.h)
                border.draw( window )
       



        border.draw( window )
        pygame.draw.line(window, WHITE, [475, 0], [475, window_height], 5)
        pygame.display.update()
        clock.tick(60) #60 FPS
        window.fill(BLACK)
        #print("end cycle")
#Ends the program/event
pygame.quit()
            
        
