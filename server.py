import sys  # In order to terminate the program
from socket import *


serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# Fill in start


serverPort = 8181

# Bind the socket localhost and port
serverSocket.bind(('localhost', serverPort))

# listen to 1 connection at the time
serverSocket.listen(1)
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1048)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
        # Fill in end
        # Send the content of the requested file to the connection socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send(b"\r\n")


        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send(b"HTTP/1.1 404 Not found\r\n")
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data