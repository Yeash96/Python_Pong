import pygame
from random import choice



window_size = window_width, window_height = 960, 540 #initial window size

class Ball(pygame.sprite.Sprite):
    
    
    def __init__( self, width = 25, height = 25, velocityX = None, velocityY = None ):
        super(Ball,self ).__init__()
       #  things needed to draw object below
        self.image = pygame.Surface( ( width, height ) )
        self.image.fill ( pygame.Color( 255, 255, 255 ) )
        self.rect = self.image.get_rect()
        #inital postion
        self.rect.centerx = window_width/2 
        self.rect.centery = window_height/2
        speedlist = [ -10, -5, -1, 1, 5,10]
        if velocityX is None:
            velocityX = choice( speedlist )
        if velocityY is None:
            velocityY = choice( speedlist )
        # velocity values
        self.hvelo = velocityX
        self.vvelo = velocityY
        

   
    def SetPostion( self, x, y ):
        #set inital postion
        self.rect.centerx = x
        self.rect.centery = y
    
    def Movement( self ):
        #change the current x,y postion by respective velocity
        self.rect.centerx += self.hvelo
        self.rect.centery += self.vvelo
        
    
    def ChangeVelocity( self, bounds ):
        #if ball left or right side is out of bounds the change velocity direction 
        if self.rect.left < bounds.left or self.rect.right > bounds.right:
            self.hvelo = -self.hvelo
        #if ball top or bottom side is out of bounds the change velocity direction     
        if self.rect.top < bounds.top or self.rect.bottom > bounds.bottom:
            self.vvelo = -self.vvelo

    def GetPositionLR( self ):
       #return tulpe with left most and right most ball postion value
       return ( self.rect.left, self.rect.right )
    
def MakeBall(  ):
    ball = Ball()
    return ball
   #====================TO DO========================================================== 
   #kill ball
   #rest ball
    
    
  
#class block for debuging
class Block( pygame.sprite.Sprite ):
    
    
    def __init__( self, width, height ):
        super(Block,self ).__init__()
        # things needed to draw object below
        self.image = pygame.Surface( ( width, height ) ) 
        self.image.fill ( pygame.Color( 0, 0, 255 ) )
        self.rect = self.image.get_rect()
        
    def SetPostion( self, x, y ):
        #set postion of block
        self.rect.x = x
        self.rect.y = y
    
# following is used to debug but should not run unless executing this file    
def balltest():
    pygame.init() #inital pygame
    running = True #while loop variable
    frames_per_seconds = 60 #fps cap
    clock = pygame.time.Clock() # clock speed
    
     #windows display  below
    pygame.display.set_caption( "Ball Test" ) # window caption

    window = pygame.display.set_mode( window_size )
    
    #''' below is border wall draw commands'''
    border=pygame.sprite.Group()
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
    ballList = []
    balls_group = pygame.sprite.Group()#create sprite group
    oneball = Ball()#create instance
    
    oneball.SetPostion( window_width/2, window_height/2 ) #set inital postion
    balls_group.add( oneball ) #add instance to sprite group
    ballList.append(oneball)
    
    zone = pygame.sprite.Group()
    leftzone = Block( 20, window_height-20)
    leftzone.SetPostion(10,10)
    leftzone.image.fill ( pygame.Color(255,0,0) )
    rightzone = Block( 20, window_height-20)
    rightzone.SetPostion( window_width-30, 10)
    rightzone.image.fill ( pygame.Color(255,0,0) )
    zone.add( leftzone, rightzone )
    zone.draw( window )
    
    
    while ( running ):
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT ):
                #print("you hit the x")
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sphere = MakeBall()
                    balls_group.add( sphere )
                    ballList.append(sphere)
                    
        border.draw( window )#comit border to window surface
        zone.draw( window )
        for balls in balls_group:
            balls.Movement()  #move ball
            
        balls_group.draw( window ) #commit the new location of the ball sprite to window surface
        #print( oneball.GetPositionLR() )#print left most and right most ball postion onto console 
        
        pygame.sprite.groupcollide( balls_group, zone, True, False )
        
        pygame.display.update() #update/ draw|display window suface 
        window.fill( pygame.Color( 0, 0, 0 ) ) #reset the screen back to blank
        #collision = pygame.sprite.spritecollideany( oneball, border )#test for collision return none if no collision
        #if collision is not None:
        #    oneball.ChangeVelocity( bounds )#change velocity
        for balls in balls_group:
            balls.ChangeVelocity( bounds )
            
            
        clock.tick( frames_per_seconds)#fps limiter
    pygame.quit()#de initalize pygame
    


if __name__ == '__main__':
    balltest()
    