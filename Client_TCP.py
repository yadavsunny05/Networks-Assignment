# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:04:27 2020

@author: ADMIN
"""

import socket
import sys
import os
import tqdm
import threading

import time
sep = "<$$$$$>"
buf_size = [1024]

nagle = True
delay = True 
host = socket.gethostname()
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if(not nagle):
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
if not delay:
       sock.setsockopt(socket.SOL_TCP, socket.TCP_QUICKACK, False)
    
start = time.time()
sock.connect((host, port))
print("Connected")
filename = "2"
sock.send(filename.encode())
pack1 = sock.recv(32).decode()

filename,filesize, = pack1.split(sep)
filesize = int(filesize)

path= r"D:\Networks Assignment\Recieved_" + filename + ".txt"

progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(path, "wb") as f:
    for _ in progress:
        bytes_read = sock.recv(buf_size[0])
        if not bytes_read:
            break
        f.write(bytes_read)
        progress.update(len(bytes_read))
sock.close()
end = time.time()
print(end - start)








    




    