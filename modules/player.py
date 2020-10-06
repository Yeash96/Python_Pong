
import pygame               # Import the backend game engine module.
import sys                  # Used to exit the game.

# Player class for pong Paddles. Inherits from pygame's Sprite class
class Player(pygame.sprite.Sprite):
    

    # Constructor that runs with defaults
    # def  __init__(self,p_Num: int = 1, width: int = 10,height: int = 40, boardDim: tuple = None, bounds: int = 40):  
    def  __init__(self,p_Num: int = 1, boardDim: tuple = None):  

        # Checks if the values passed for the player num are appropriate.
        if p_Num > 2 or p_Num < 1:
            print("Improper character value passed. Please pass a \"1\" or \"2\".")
            pygame.quit()
            sys.exit()

        if not boardDim:
            print("Please pass board dimensions as a tuple: (x,y).")
            pygame.quit()
            sys.exit()            
            
        # Run the constructor of the parent class to initialize other factors
        super().__init__()  

        self.x_Board, self.y_Board = boardDim

        # Create a limiter for how  much buffer space is between the the end points of the sprite and the game window's walls.
        self.bounds = self.x_Board *4/ 75
        self.width = self.bounds/4

        # Create the sprite for the character paddle onto the surface of the game window with the appropriate dimensions.
        self.image = pygame.Surface((self.width, self.bounds))
        # Set the default player paddle color to white.
        self.color = pygame.Color(255, 255, 255)
        self.image.fill (self.color)
        # Use the dimensions to establish the sprite's shape:
        self.rect = self.image.get_rect()
        
        # Store data of which player this is.
        self.p_Num = p_Num

        self.speed = 12



        # board/windows parameters

        # Establish the default position of each player
        if self.p_Num == 1:
            self.def_x_pos = self.x_Board  // 10     
            self.def_y_pos = self.y_Board  // 2
            
        else:
            self.def_x_pos = self.x_Board  * 9 // 10     
            self.def_y_pos = self.y_Board  // 2
        
        # Starts each player sprite in the default position.
        self.setPos(self.def_x_pos,self.def_y_pos)


    # Used to reset the position of the paddles to their default positions. Should be used after each score and game initialization.
    def defPos(self):
        self.rect.centerx = self.def_x_pos
        self.rect.centery = self.def_y_pos

    # Function used to set the player sprites to any place in the display window if needed.
    def setPos(self, x: int, y: int):
        self.rect.centerx = x
        self.rect.centery = y
      
    def setPosinGame(self,p_Num: int = 1, boardDim: tuple = None,):
        self.x_Board, self.y_Board = boardDim
        print(self.x_Board)
        if self.p_Num == 1:
            self.def_x_pos = self.x_Board  // 10     
            self.def_y_pos = self.y_Board  // 2
            
        else:
            self.def_x_pos = self.x_Board  * 9 // 10     
            self.def_y_pos = self.y_Board  // 2
                # Create the sprite for the character paddle onto the surface of the game window with the appropriate dimensions.
        self.image = pygame.Surface((self.width, self.bounds))
        # Set the default player paddle color to white.
        self.color = pygame.Color(255, 255, 255)
        self.image.fill (self.color)
        # Use the dimensions to establish the sprite's shape:
        self.rect = self.image.get_rect()
        self.setPos(self.def_x_pos,self.def_y_pos)

    # Function is called whenever input is given
    # TODO: Modify this so that it reads the input and does the movement making within the function.
    def move(self):
        # Movemnets are only vertical
        pressed = pygame.key.get_pressed()
        
        # Does not allow movement further than the limit established - based on the position of the center of the sprite.
        # if self.rect.centery >= self.y_Board - self.bounds:
        #     if pressed[pygame.K_w] or pressed[pygame.K_UP]:
        #         self.rect.centery -= self.speed     
        # elif self.rect.centery <= 0 + self.bounds:
        #     if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        #         self.rect.centery += self.speed       
        # else:
        #     if pressed[pygame.K_w] or pressed[pygame.K_UP]:
        #         self.rect.centery -= self.speed
        #     elif pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        #         self.rect.centery += self.speed

        if self.p_Num == 1:
            if self.rect.centery >= self.y_Board - self.bounds:
                if pressed[pygame.K_w]:
                    self.rect.centery -= self.speed     
            elif self.rect.centery <= 0 + self.bounds:
                if pressed[pygame.K_s]:
                    self.rect.centery += self.speed       
            else:
                if pressed[pygame.K_w]:
                    self.rect.centery -= self.speed
                elif pressed[pygame.K_s]:
                    self.rect.centery += self.speed        
        else:
            if self.rect.centery >= self.y_Board - self.bounds:
                if pressed[pygame.K_UP]:
                    self.rect.centery -= self.speed     
            elif self.rect.centery <= 0 + self.bounds:
                if pressed[pygame.K_DOWN]:
                    self.rect.centery += self.speed       
            else:
                if pressed[pygame.K_UP]:
                    self.rect.centery -= self.speed
                elif pressed[pygame.K_DOWN]:
                    self.rect.centery += self.speed


    def draw(self,win):
        win.fill(pygame.Color(0,0,0))
        pygame.draw.rect(win, self.color, self.rect)

        
            


