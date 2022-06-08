# Citation for the following program:
# Date: 4/17/2022
# Based on TCPServer.py from chapter 2.7.2 of the book Computer Networking: A Top-Down Approach
# Modified from my implementation of simple_server.py from the A1
# Authors: Jim Kurose, Keith Ross

# Usage: custom port number entry at the CLI
# Source: https://www.tutorialspoint.com/python/python_command_line_arguments.htm
from sys import argv
from socket import *

HOST = 'localhost'


class ChatServer:
    def __init__(self, port=1238):
        self._server_socket = None
        self._connection_socket = None

        self.bind_server_socket(port)
        self.set_listen(port)
        self.accept_connection()

    def bind_server_socket(self, port):
        """
        1. The server creates a socket and binds to 'localhost' and port xxxx
        """
        self._server_socket = socket(AF_INET, SOCK_STREAM)
        self._server_socket.bind((HOST, port))

    def set_listen(self, port):
        """
        2. The server then listens for a connection
        """
        self._server_socket.listen(1)
        print("Server listening on: {} on port: {}".format(HOST, port))

    def accept_connection(self):
        """
        2.5. The server accepts the connection
        """
        self._connection_socket, addr = self._server_socket.accept()
        print("Connected by: {}".format(addr))
        print("Waiting for message...")

    def run(self):
        """
        7. Back to step 3
        Handles the recv/input/send loop
        """
        while True:
            message = ""

            # 3. When connected, the server calls recv to receive data
            message = self._connection_socket.recv(1024)
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
        """
        Sockets are closed
        """
        self._connection_socket.close()
        self._server_socket.close()


def main():
    if len(argv) == 2:
        chat_server = ChatServer(int(argv[1]))
    else:
        chat_server = ChatServer()
    chat_server.run()


main()
