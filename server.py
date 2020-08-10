# This is Khrystarlite's signature hugging rabbit.
print(" () ()")
print("<('w')>")

# This scratch file contains the main loop that initializes pygame and used the modules to run the game.


# Python packages
import pygame               # Python game creation framework - the main backend.
import asyncio, socket, sys
from _thread import start_new_thread
from modules import Player, Network  # Player module for the pong paddles.


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True: 
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Recveived:", reply)
                print("Sending:", reply)
            
            conn.sendall(str.encode(reply))
        except:
            break
    
    print("Lost connection")
    conn.close()

# The main loop.
def main():

    server = "192.168.1.245"
    port = 5555
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.bind((server,port))
    except socket.error as e:
        print(e)
    
    s.listen(8)
    print("Server started. Waiting for connection.")

    

    

        

    # Create static variables:
    fps = 60                    # The standard frames per second - limited so that the game does not automatically 
                                #   use all system resources.
    p_Speed = 12                # The current speed the player paddles move at.
    win_W, win_H = 960, 540     # Dimensions for the current game window.
    clock = pygame.time.Clock() # Used with fps variable to limit the fps of the game.

    bg_Color = pygame.Color(0,0,0)


    # Initialize pygame and its assets so they can be used
    pygame.init() 

    # Create player objects for the paddles.
    p1 = Player(1, boardDim=(win_W, win_H))
    p2 = Player(2, boardDim=(win_W, win_H))

    # create an object that represents the display window.
    window = pygame.display.set_mode( (win_W, win_H) )

    # Test window title.
    pygame.display.set_caption( "Player Test" ) 
    
    # Create a group of sprites that will update with inputs and display movement
    player_Group = pygame.sprite.Group()  
    player_Group.add(p1)
    player_Group.add(p2)

    # The main game loop. Runs until the exit button is clicked. May add exit function within main menu.
    while True:

        conn, addr = s.accept()
        print("Connecter to: ", addr)
        start_new_thread(threaded_client, (conn,))



        # # Checks if the game is exited.
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT : 
        #         pygame.quit()
        #         sys.exit()

        # # pygame will listen for keyboard inputs.
        # #   May be moved to player class later
        # # pressed = pygame.key.get_pressed()

        # p1.move()
        # p2.move()
        
        
        
        # # Draws the player sprites to the display window
        # # player_Group.draw(window)
        # p1.draw(window)
        # p2.draw(window)
        # # Updates the display window whenever the sprites update
        # pygame.display.update()
        # # Updates the window so that areas where sprites were previouslyu return to the display window's background color.
        # window.fill(bg_Color)
        # # Limits FPS to 60
        # clock.tick(fps)
        # # print(p2.rect.right)

        


# Runs the main function  when the program is run
if __name__ == '__main__':
    main()