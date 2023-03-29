import socket

# Create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the IP address of the server (this assumes the server has a static IP address)
server_ip = "192.168.0.222"  # Change this to the actual IP address of the server

# Connect to the server on port 333
clientsocket.connect((server_ip, 333))

# Send a message to the server
message = "Hello server!"
clientsocket.send(message.encode())

# Close the socket
clientsocket.close()
