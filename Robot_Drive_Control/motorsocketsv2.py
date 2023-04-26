import socket

class MotorServer:
    def __init__(self,ip='127.0.0.1', port = 12345):
        self.ip, self.port = ip, port 
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP socket
        self.sock.bind((self.ip,self.port))  # Local host
    
    # Returns channel and value recieved through socket
    def recv(self, bytesbuffer = 5): 
        data, addr = self.sock.recvfrom(bytesbuffer)
        channel, val = map(int,data.decode().split(","))        #data comes in the string format "channel,value"
        return channel, val


class MotorClient:
    def __init__(self, channel_id = 0, ip='192.168.1.103', port = 12345):
        self.ip, self.port = ip, port 
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP socket
        self.channel = channel_id

    #Appends message with motor channel and sends through socket
    def send(self, msg:str):
        msg = str(self.channel) + ',' + msg                         
        self.client_socket.sendto(msg.encode("utf-8"),(self.ip,self.port))       

    #send the motor value to the motor
    def write(self, val:int):    
        self.send(str(val))




