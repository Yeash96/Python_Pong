# This is Khrystarlite's signature hugging rabbit.
print(" () ()")
print("<('w')>")

# This scratch file contains the main loop that initializes pygame and used the modules to run the game.


# Python packages
import socket, sys
from _thread import start_new_thread
# from modules import Player2, Network  # Player module for the pong paddles.
# The main loop.

current_Player = 0
win_W, win_H = 960, 540     # Dimensions for the current game window.

# pos = [(1/10,1/2),(9/10,1/2)]
pos = [(win_W//10, win_H//2),(win_W*9//10,win_H//2)]

hostname = socket.gethostname()

server = socket.gethostbyname(hostname)
# server = "192.168.1.245"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    print(e)

s.listen(2)
print("Server started. Waiting for connection.")





def read_Pos(string: str):
    print(string)
    string = string.split(",")
    return int(string[0]), int(string[1])
def make_pos(p_pos: tuple):
    return str(p_pos[0]) + "," + str(p_pos[1])


def threaded_client(conn,current_Player):
    # print("Current Player: ", current_Player)
    conn.send(str.encode(make_pos(pos[current_Player])))
    reply = ""
    # print("HIT")
    while True: 
        try:
            # print(1)
            data = read_Pos(conn.recv(2048).decode())
            # print(2)
            pos[current_Player] = data
            # print ("POS in server:", pos)
           
            if not data:
                print("Disconnected")
                break
            else:
                if current_Player == 0:
                    reply = (0,pos[1])

                elif current_Player == 1:
                    reply = (1,pos[0])
                else:
                    reply = (current_Player,pos)

            print("Recveived:", data)
            print("Sending:", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except:
            # print("except", reply)
            break
    
    print("Lost connection")
    current_Player -= 1
    conn.close()
    
    


    


while True:
    connection, address = s.accept()
    print("Connected to:", address)

    start_new_thread(threaded_client, (connection, current_Player))
    current_Player += 1

    

