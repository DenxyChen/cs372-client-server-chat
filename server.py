# Citation for the following program:
# Date: 4/17/2022
# Based on TCPServer.py from chapter 2.7.2 of the book Computer Networking: A Top-Down Approach
# Modified from my implementation of simple_server.py from the A1
# Authors: Jim Kurose, Keith Ross

from socket import *


def main():
    # 1. The server creates a socket and binds to 'localhost' and port xxxx
    host = "localhost"
    port = 5000
    source = (host, port)

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(source)

    # 2. The server then listens for a connection
    server_socket.listen(1)
    print("Server listening on: {} on port: {}".format(host, port))

    connection_socket, addr = server_socket.accept()
    print("Connected by: {}".format(source))
    print("Waiting for message...")

    # 7. Back to step 3
    while True:
        message = ""

        # 3. When connected, the server calls recv to receive data
        message = connection_socket.recv(1024)
        if len(message) == 0:
            break

        # 4. The server prints the data, then prompts for a reply
        print(message.decode())
        print("Type /q to quit")
        print("Enter message to send ...")
        reply = input(">")

        # 5. If the reply is /q, the server quits
        if reply == "/q":
            break

        # 6. Otherwise the server sends the reply
        connection_socket.send(reply.encode())

    # 8. Sockets are closed
    connection_socket.close()
    server_socket.close()
