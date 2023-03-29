import socket

# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the IP address of the server (this assumes the server has a static IP address)
server_ip = "192.168.0.222"  # Change this to the actual IP address of the server

# Bind the socket to the IP address and port 333
serversocket.bind((server_ip, 333))

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
