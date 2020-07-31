

class Player:
    # Player class for pong. Only 
    import pygetwindow as gw

    
    def  __init__(self,p_Num: int =0, boardDim: tuple =None):    

        if p_Num > 1 or p_Num < 0:
            print("Improper character value passed. Please pass a \"1\" or \"2\".")
            exit(1)

        self.p_Num = p_Num

        if not boardDim:
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
        self.x_pos = self.def_x_pos
        self.y_pos = self.def_y_pos
        pass    

    def setPos(self, x, y):

        self.x_pos = x
        self.y_pos = y

        pass

    def move(self,x_move=0, y_move = 0):
        self.x_pos += x_move
        self.y_pos += y_move



    
