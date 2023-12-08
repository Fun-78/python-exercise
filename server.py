import socket

server = socket.socket() # by default creating tcp and ipv4 connection
print('socket created')
server.bind(('localhost', 9999))

server.listen(5)
print('waiting for connection')

while True:
    client, addr = server.accept()
    print('connecte witj', addr)
    client.send(bytes('You are welcome am Lian and you? ', 'utf-8'))
    name = client.recv(1024).decode()
    #client.send(bytes('You are welcome am Lian and you? ', 'utf-8'))
    resp = "glad to talk with u " + name
    client.send(bytes(resp, 'utf-8'))
    

    



'''
print('socket created')

s.bind('localhost', 192.168.0.101)

s.listen(3)
print('waiting for connection')

while True:
    c, addr = s.accept()
    print('connected with', addr)

    c.send(bytes('welcome to socket','uft-8'))
    c.close()
    '''