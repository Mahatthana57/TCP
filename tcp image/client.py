#!/usr/bin/env python

import socket

image = 'testImg.jpg'

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 409600000
MESSAGE = "Srnt image to server"

#Open img file
myImage = open(image, 'rb')
bytesOf = myImage.read()
myImage.close()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(bytesOf)

finally:
    s.close()

