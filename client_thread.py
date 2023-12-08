import time
import socket

client = socket.socket()

client.connect(('localhost', 9998))
name = input('enter required food ')
client.send(bytes(name, 'utf-8'))
message = client.recv(1024).decode()
print(message)

