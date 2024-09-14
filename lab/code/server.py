#Problem #6
import socket
import sys

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


port = 6789
serverSocket.bind(('', port))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

print('The server is ready to receive')

while True:
    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    try:
        # Receives the request message from the client
        message = connectionSocket.recv(1024).decode()

        # Extract the path of the requested object from the message
        filename = message.split()[1]
        f = open(filename[1:])

        # Store the entire content of the requested file in a temporary buffer
        outputdata = f.read()

        # Send the HTTP response header line to the connection socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send the content of the requested file to the connection socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
    # Send HTTP response message for the file not found
            header = "HTTP/1.1 404 Not Found\r\n\r\n"
            connectionSocket.send(header.encode())
            connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())

    # Close the client connection socket
            connectionSocket.close()


# Close the server socket
serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data


