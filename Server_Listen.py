import socket
import sys

HOST = ''        # Symbolic name, meaning all available interfaces
PORT = 1234      # Arbitrary non-privileged port

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a public host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)
print('Waiting for client connection...')

# Accept a new connection
client_socket, client_address = server_socket.accept()
print('Connected by', client_address)

while True:
    try:
        # Receive data from the client
        data = client_socket.recv(1024)
        if data:
            print(data.decode())
        else:
            # Connection closed by client
            print('Connection closed by client')
            client_socket.close()
            server_socket.close()
            sys.exit()

    except:
        # Error occurred while receiving data
        print('Error occurred while receiving data')
        client_socket.close()
        server_socket.close()
        sys.exit()
