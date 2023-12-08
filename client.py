import socket

client = socket.socket()

client.connect(('localhost', 9999))

message = client.recv(1024).decode()
print(message)

name  = input('enter ur name ')
client.send(bytes(name,'utf-8'))

message2 = client.recv(1024).decode()
print(message2)
