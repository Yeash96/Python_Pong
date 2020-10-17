import socket

class Network:
    def __init__(self):
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.hostname = socket.gethostname()
        self.server = socket.gethostbyname(self.hostname)
        # print("Network server:\t", self.server)
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        # print(self.pos)
        # print(self.id)
        self.buffer = 2048


    def getPos(self):
        return self.pos
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(self.buffer).decode()
        except:
            pass
    
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(self.buffer).decode()
        except socket.error as e:
            print(e)

    def getPosSpect(self):
        try:
            return self.client.recv(self.buffer).decode()
        except socket.error as e:
            print(e)

# n = Network()
# print(n.send("hellow"))
# print(n.send("world"))
# print(n.send("pizza"))