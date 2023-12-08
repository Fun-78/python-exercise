import socket
import tqdm
import os

os.chdir('c:\\Users\\user\\Desktop\\NOTES\\Level 3\\Introduction to python') #destination foldder

separator = '#'
buffer_size = 4096
host = '197.168.43.80'
port = 5001
filename = ''
filesize = os.path.getsize(filename)

s = socket.socket()
print(f'connecting to {host} : {port}')
s.connect((host, port))
print('conected')
s.send(f'{filename}{separator}{filesize}'.encode())
#start sending file
progress = tqdm.tqdm(range(filesize), f'sending {filename}', unit ='8', unit_scale=True, unit_divisor=1024)
with open(filename, 'r') as f:
    while True:
        bytes_read = f.read(buffer_size)
        if not bytes_read:
            break
        s.sendall(bytes_read)
        progress.update(len(bytes_read))
        s.close()
