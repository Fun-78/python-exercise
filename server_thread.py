from collections.abc import Callable, Iterable, Mapping
import socket
import time 
import threading
from typing import Any

class threadforclient(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        name = self.client.recv(1024).decode()
        if name == 'couscous':
                    time.sleep(20)
        if name == 'riz':
              time.sleep(10)
        if name == 'haricot':
              time.sleep(30)

        self.client.send(bytes('votre plat' + name + 'est servi'))
        self.client.close()


server = socket.socket()
print('created')
server.bind(('localhost', 9998))
server.listen(3)
print('waiting for connection')

while True:
      client, address = server.accept()
      myclient = threadforclient(client)
      myclient.start()
      server.close()



              


              