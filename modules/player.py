
import pygame
# Player class for pong. Only 
import pygetwindow as gw    

class Player(pygame.sprite.Sprite):
    

    
    def  __init__(self,p_Num: int =0, width: int = 10,height: int = 40, boardDim: tuple =None):  


        if p_Num > 1 or p_Num < 0:
            print("Improper character value passed. Please pass a \"1\" or \"2\".")
            pygame.QUIT
            
        super().__init__()  
        self.h_lim = height

        self.image = pygame.Surface((width, height))
        self.image.fill (pygame.Color(255, 255, 255))
        self.rect = self.image.get_rect()

        self.p_Num = p_Num

        if not boardDim:
            # self.x_Board, self.y_Board = gw.getActiveWindow().size
            self.x_Board, self.y_Board = gw.getActiveWindow().size
        else:
            self.x_Board, self.y_Board = boardDim

        # board/windows parameters

    

        if self.p_Num == 0:
            self.def_x_pos = self.x_Board  // 10     
            self.def_y_pos = self.y_Board  // 2
        else:
            self.def_x_pos = self.x_Board  * 9 // 10     
            self.def_y_pos = self.y_Board  // 2
        
        self.setPos(self.def_x_pos,self.def_y_pos)


    
    def defPos(self):
        self.rect.centerx = self.def_x_pos
        self.rect.centery = self.def_y_pos
        pass    

    def setPos(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y

        pass

    def getPos(self):
        return (self.rect.centerx, self.rect.centery)

    def move(self, y_move):
        # Movemnets are only vertical
        # self.x_pos += x_move
        if self.rect.centery >= self.y_Board - self.h_lim and y_move > 0:
            pass
        
        elif self.rect.centery <= 0 + self.h_lim and y_move < 0:
            pass          
        else:
            self.rect.centery += y_move



    
