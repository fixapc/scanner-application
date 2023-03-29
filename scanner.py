import socket

# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Bind the socket to a public host and port 333
serversocket.bind((host, 333))

# Set the server to listen on port 333
serversocket.listen(5)

while True:
    # Wait for a client connection
    clientsocket, addr = serversocket.accept()
    
    # Receive data from the client
    data = clientsocket.recv(1024)
    
    # Print out the received data
    print("Received from {}: {}".format(addr, data.decode()))

    # Close the client socket
    clientsocket.close()
