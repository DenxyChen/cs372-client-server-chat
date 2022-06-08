# Citation for the following program:
# Date: 6/7/2022
# Based on TCPServer.py from chapter 2.7.2 of the book Computer Networking: A Top-Down Approach
# Authors: Jim Kurose, Keith Ross
# Modified from my implementation of simple_server.py from A1
# Additional sources: https://www.tutorialkart.com/python/how-to-find-length-of-bytes-in-python/ for length of bytes
# https://docs.python.org/3.4/howto/sockets.html for more information on connecting and closing sockets

# Usage: custom port number entry at the CLI
# Source: https://www.tutorialspoint.com/python/python_command_line_arguments.htm
from sys import argv
from socket import *

HOST = 'localhost'
SIZE = 2048


class ChatServer:
    """
    Implementation of a chat server object. Not used.
    """
    def __init__(self, port=1238):
        self._server_socket = None
        self._connection_socket = None

        self.bind_server_socket(port)
        self.set_listen(port)
        self.accept_connection()

    def bind_server_socket(self, port):
        self._server_socket = socket(AF_INET, SOCK_STREAM)
        self._server_socket.bind((HOST, port))

    def set_listen(self, port):
        self._server_socket.listen(1)
        print("Server listening on: {} on port: {}".format(HOST, port))

    def accept_connection(self):
        self._connection_socket, addr = self._server_socket.accept()
        print("Connected by: {}".format(addr))
        print("Waiting for message...")

    def run(self):
        while True:
            message = ""

            # 3. When connected, the server calls recv to receive data
            message = self._connection_socket.recv(SIZE)
            if len(message) == 0:
                return self.close_connections()

            # 4. The server prints the data, then prompts for a reply
            print(message.decode())
            print("Type /q to quit")
            print("Enter message to send ...")
            reply = input(">")

            # 5. If the reply is /q, the server quits
            if reply == "/q":
                return self.close_connections()

            # 6. Otherwise the server sends the reply
            self._connection_socket.send(reply.encode())

    def close_connections(self):
        self._connection_socket.close()
        self._server_socket.close()


def main(port=1238):
    handshake = True

    # 1. The server creates a socket and binds to 'localhost' and port xxxx
    source = (HOST, port)
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(source)

    # 2. The server then listens for a connection
    server_socket.listen(1)
    print("Server listening on: {} on port: {}".format(HOST, port))

    connection_socket, addr = server_socket.accept()
    print("Connected by: {}".format(addr))
    print("Waiting for message...")

    # 7. Back to step 3
    while True:
        # 3. When connected, the server calls recv to receive data
        message = connection_socket.recv(SIZE)

        # If the connection was closed by the client, the length of the message will be 0
        if len(message) == 0:
            break

        # 4. The server prints the data, then prompts for a reply
        print(message.decode())
        if handshake:
            print("Type /q to quit")
            print("Enter message to send ...")
            handshake = False
        reply = input(">")

        # 5. If the reply is /q, the server quits
        if reply == "/q":
            break

        # 6. Otherwise the server sends the reply
        connection_socket.send(reply.encode())

    # 8. Sockets are closed
    connection_socket.close()
    server_socket.close()


# Runs the program with an optionally selected port
if len(argv) == 2:
    main(int(argv[1]))
else:
    main()
