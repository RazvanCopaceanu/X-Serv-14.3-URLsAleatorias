#!/usr/bin/python3

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 3456))
mySocket.listen(5)

aleatorio = str(random.randint(0, 1000000))

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2048))
        print('Answering back...')
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h2>Hola! " +
                        "<a href=" + aleatorio + ">Dame otra</a>" +
                        "</h2></body></html>" +
                        "\r\n", "utf-8"))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
