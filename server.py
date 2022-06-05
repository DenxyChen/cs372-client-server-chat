# Citation for the following program:
# Date: 4/17/2022
# Based on TCPServer.py from chapter 2.7.2 of the book Computer Networking: A Top-Down Approach
# Modified from my implementation of simple_server.py from the first programming assignment
# Authors: Jim Kurose, Keith Ross

from socket import *

# Source host and port required for connection
host = "localhost"
port = 5000
source = (host, port)

# Establish TCP server socket which awaits a client connection
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(source)
server_socket.listen(1)

# HTTP data to be sent to client
response = ""

while True:
    # Handshakes with the client by establishing a TCP connection with a dedicated socket
    connection_socket, addr = server_socket.accept()
    print("Connected by: {}".format(source))

    # Receives an HTTP request from the client
    request = connection_socket.recv(1024)
    print("\nRecieved: {}".format(request))

    print("Enter message to send ...")
    response = input(">")

    # Encodes the HTML into bytes and sends it to the client in response
    print("\nSending >>>>>>>>>>\n{}".format(response))
    connection_socket.send(response.encode())
    print("<<<<<<<<<<")

    # Close the dedicated connection once all data has been sent
    connection_socket.close()


