import pygame

class Spectator(pygame.sprite.Sprite):
    

    # Constructor that runs with defaults
    # def  __init__(self,p_Num: int = 1, width: int = 10,height: int = 40, boardDim: tuple = None, bounds: int = 40):  
    def  __init__(self,p_Num: int=0, boardDim: tuple = None):  
     
            
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