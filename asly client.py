name = ' sami '
from threading import Thread
import _thread
import socket
soc = socket.socket()
import time
host = '127.0.0.1'
port = 8887

soc.connect((host, port))
def send_thread(soc, x):
    
    soc.sendall(x.encode())
        
    
def recv_thread(soc):
    while True:
        print('recv ')
        recv = soc.recv(1024).decode()
        
        print(recv)
        
         
recv = Thread(target=recv_thread, args=(soc,))
recv.start()
while True:
    print('send')
    x = input()
    _thread.start_new_thread(send_thread, (soc, name + x,))


input()
