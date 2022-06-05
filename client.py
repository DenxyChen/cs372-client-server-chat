# Citation for the following program:
# Date: 4/17/2022
# Based on TCPClient.py from chapter 2.7.2 of the book Computer Networking: A Top-Down Approach
# Modified from my simple_client.py implementation from the first programming assignment
# Authors: Jim Kurose, Keith Ross
# Additional sources: https://www.tutorialkart.com/python/how-to-find-length-of-bytes-in-python/ for length of bytes

from socket import *

# Target host and port required for connection
host = "localhost"
port = 5000

print("Connected to: {} on port: {}".format(host, port))
print("Type \q to quit")

# Establish TCP client socket and establish a connection with the server
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((host, port))

# Send the UTF-8 encoded request string
print("Enter a message to send...")
request = ""

while True:
    client_socket.send(request.encode())
    request = input(">")

    if request == "\q":
        break

    # Read up to 1024 bytes of the response and display the decoded string and its length
    response = client_socket.recv(1024)
    print("[RECV] - length: {}".format(len(response)))
    print(response.decode())

# Close the client-server connection
client_socket.close()