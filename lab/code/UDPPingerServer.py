import random
from socket import *

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

while True:
    randomInteger = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    message = message.upper()
    # If int is less than 4, the packet is lost and do not respond
    if randomInteger < 4:
        continue
    # Otherwise, the server responds
    serverSocket.sendto(message, address)
