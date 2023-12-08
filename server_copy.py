import socket
import tqdm
import os

os.chdir('c:\\Users\\user\\Desktop\\NOTES\\Level 3\\Introduction to python') #destination foldder
#deveice ip addr
server_host = 'localhost'
server_port = 5001

buffer_size = 4096
separator = '#'
s = socket.socket()
s.bind((server_host, server_port))
s.listen(5)
print(f'listening as {server_host} : {server_port}')
client_socket, address =s.accept()
#if below code is executed means sender is connected
print(f'{address} is connected')

received = client_socket.recv(buffer_size).decode()
filename, filesize = received.split(separator)
#remove absolute path if there is
filename = os.path.basename(filename)
#convert to interger
filesize = int(filesize)

progress = tqdm.tqdm(range(filesize), f'receiving {filename}', unit ='8', unit_scale=True, unit_divisor=5)
with open (filename, 'wb') as f:
    while True:
        bytes_read = client_socket.recv(buffer_size)
        if not bytes_read:
            break
        f.write(bytes_read)
        progress.update(len(bytes_read))

client_socket.close()
s.close()

