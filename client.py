# Citation for the following program:
# Date: 6/7/2022
# Based on TCPClient.py from chapter 2.7.2 of the book Computer Networking: A Top-Down Approach
# Modified from my simple_client.py implementation from the first programming assignment
# Authors: Jim Kurose, Keith Ross
# Additional sources: https://www.tutorialkart.com/python/how-to-find-length-of-bytes-in-python/ for length of bytes

# Usage: custom port number entry at the CLI
# Source: https://www.tutorialspoint.com/python/python_command_line_arguments.htm
from sys import argv
from socket import *

HOST = 'localhost'


class ChatClient:
    def __init__(self, port=1238):
        self._client_socket = None

        self.connect_to_server(port)

    def connect_to_server(self, port):
        """
        1. The client creates a socket and connects to 'localhost' and port xxxx
        """
        self._client_socket = socket(AF_INET, SOCK_STREAM)
        self._client_socket.connect((HOST, port))
        print("Connected to: {} on port: {}".format(HOST, port))
        print("Type \q to quit")
        print("Enter a message to send...")

    def run(self):
        """
        7. Back to step 2
        Handles the input/send/recv/print loop
        """
        while True:
            # 2. When connected, the client prompts for a message to send
            message = input(">")

            # 3. If the message is /q, the client quits
            if message == "/q":
                break

            # 4. Otherwise, the client sends the message
            self._client_socket.send(message.encode())

            # 5. The client calls recv to receive data
            reply = self._client_socket.recv(1024)
            if len(reply) == 0:
                break

            # 6. The client prints the data
            print(reply.decode())

    def close_connection(self):
        self._client_socket.close()


def main(port=1238):
    # 1. The client creates a socket and connects to 'localhost' and port xxxx
    source = (HOST, port)

    client_socket = socket(AF_INET, SOCK_STREAM)

    # Usage: error handling
    # https://stackoverflow.com/questions/1483429/how-to-print-an-exception-in-python
    try:
        client_socket.connect(source)
    except ConnectionRefusedError as e:
        print("client.py: {} on port {} is not an active server".format(HOST, port))
        print(e)
        return

    print("Connected to: {} on port: {}".format(HOST, port))
    print("Type \q to quit")
    print("Enter a message to send...")

    # 7. Back to step 2
    while True:
        # 2. When connected, the client prompts for a message to send
        message = input(">")

        # 3. If the message is /q, the client quits
        if message == "/q":
            break

        # 4. Otherwise, the client sends the message
        client_socket.send(message.encode())

        # 5. The client calls recv to receive data
        reply = client_socket.recv(1024)
        if len(reply) == 0:
            break

        # 6. The client prints the data
        print(reply.decode())

    # 8. Sockets are closed
    client_socket.close()


if len(argv) == 2:
    main(int(argv[1]))
else:
    main()
