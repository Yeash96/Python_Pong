#!/usr/bin/env python

from modules import *

import pygame
import sys

def pong( ):
    running = True #game status
    frames_per_seconds = 60 #fps
    pygame.init() #inital pygame
    clock = pygame.time.Clock() #clock speed variable
    window_size = window_width, window_height = 960, 540 #initial window size
    #create window
    pygame.display.set_caption( "PONG" ) # window caption
    window = pygame.display.set_mode ((window_size), pygame.RESIZABLE)
    
    #''' below is border wall draw commands'''
    border=pygame.sprite.Group() #make a border group
    topwall = Block( window_width, 10 )
    topwall.SetPostion( 0, 0 )
    bottomwall = Block( window_width, 10 )
    bottomwall.SetPostion( 0, window_height-10 )
    leftwall = Block( 10, window_height )
    leftwall.SetPostion( 0, 0 )
    rightwall = Block( 10, window_height )
    rightwall.SetPostion( window_width-10, 0 )
    border.add( topwall, bottomwall, leftwall, rightwall )
    bounds = pygame.Rect( 10, 10, window_width-20, window_height-20 ) #create rect value of the playing feild used to find border collisions
    
                        # ( top, left, bottom, right)
   #'''below is ball draw instruction'''
    #ballList = []
    balls_group = pygame.sprite.Group()#create sprite group
    oneball = Ball()#create instance
    
    oneball.SetPostion( window_width/2, window_height/2 ) #set inital postion
    balls_group.add( oneball ) #add instance to sprite group
    #ballList.append(oneball)
    
    #Below is the score zone group
    zone = pygame.sprite.Group()
    leftzone = Block( 20, window_height-20)
    leftzone.SetPostion(10,10)
    leftzone.image.fill ( pygame.Color(255,0,0) )
    rightzone = Block( 20, window_height-20)
    rightzone.SetPostion( window_width-30, 10)
    rightzone.image.fill ( pygame.Color(255,0,0) )
    zone.add( leftzone, rightzone )
    zone.draw( window )
    
    
    #Create Players
    p1 = Player(1, boardDim=(window_width, window_height))
    p2 = Player(2, boardDim=(window_width, window_height))
    # Create a group of sprites that will update with inputs and display movement
    player_Group = pygame.sprite.Group()  
    player_Group.add(p1)
    player_Group.add(p2)
    
    score1 = 0
    score2 = 0
    font = pygame.font.Font(None, 74)
    
    while ( running) :
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT ):#if top right x is hit
                running = False
                
            elif event.type ==  pygame.VIDEORESIZE:#if resizing the window was attempted
                window = pygame.display.set_mode (( event.w, event.h ), pygame.RESIZABLE)

                window_size = window_width, window_height = event.w, event.h #update  window size
                
                topwall.UpdateSize( window_width, 10 )
                topwall.SetPostion( 0, 0 )
                bottomwall.UpdateSize( window_width, 10 )
                bottomwall.SetPostion( 0, window_height-10 )
                leftwall.UpdateSize( 10, window_height )
                leftwall.SetPostion( 0, 0 )
                rightwall.UpdateSize( 10, window_height )
                rightwall.SetPostion( window_width-10, 0 )
                
                bounds = pygame.Rect( 10, 10, window_width-20, window_height-20 )
                
                leftzone.UpdateSize( 20, window_height-20)
                leftzone.SetPostion(10,10)
                leftzone.image.fill ( pygame.Color(255,0,0) )
                rightzone.UpdateSize( 20, window_height-20)
                rightzone.SetPostion( window_width-30, 10)
                rightzone.image.fill ( pygame.Color(255,0,0) ) 
                
                p1.setPosinGame(1, boardDim=(window_width, window_height))
                p2.setPosinGame(2, boardDim=(window_width, window_height))
                
                               
            elif event.type == pygame.KEYDOWN: #if space is hit spawn new ball
                if event.key == pygame.K_SPACE:
                    sphere = MakeBall()
                    balls_group.add( sphere )
                    
        p1.move()
        p2.move()
           
        for balls in balls_group:
            balls.Movement()  #move ball
        
        for balls in balls_group:
            balls.ChangeVelocity( bounds )
        
        for balls in balls_group: #check collisions
           if balls.rect.colliderect(p2.rect) == 1:
                balls.Paddle()
                #print("collision")
           elif balls.rect.colliderect(p1.rect) == 1:
                balls.Paddle()
                #print("collision")
                
           elif balls.rect.colliderect(leftzone.rect) == 1:
                balls.Paddle()
                #print("Goal!")
                score1 += 1 
           elif balls.rect.colliderect(rightzone.rect) == 1:
                balls.Paddle()
                #print("Goal!") 
                score2 += 1  
        pygame.sprite.groupcollide( balls_group, zone, True, False )    
                
                
         #update score       
        text1 = font.render(str(score1), 1, (255, 255, 255))
        text2 = font.render(str(score2), 1, (255, 255, 255))

        #draw new information on window
        border.draw( window )#comit border to window surface
        zone.draw( window )
        balls_group.draw( window ) #commit the new location of the ball sprite to window surface
        player_Group.draw(window)    
        window.blit(text1, (240,30))   
        window.blit(text2, (window_width-240,30))    
            
        pygame.display.update() #update/ draw|display window suface 
        window.fill( pygame.Color( 0, 0, 0 ) )#clear window
        clock.tick( frames_per_seconds)#fps limiter
        
    pygame.quit()#de initalize pygame
    sys.exit()


if __name__ == '__main__':
    pong()
    