# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 03:34:04 2020

@author: ADMIN
"""

import socket
import sys
import os
import tqdm
import threading
import time

time.sleep(5)
sep = "<$$$$$>"
buf_size = [1024]


    
host = socket.gethostname()
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.settimeout(30)

start = time.time()
# sock.connect((host, port))

sock.sendto("".encode(), (host,port))
name = "Moby-Dick; or, The Whale by Herman Melville"

sock.sendto("Moby-Dick; or, The Whale by Herman Melville".encode(), (host,port))
print("Connected")
pack1 = sock.recv(max(buf_size[0],32)).decode()

filename,filesize = pack1.split(sep)
filesize = int(filesize)

path= r"D:\Networks Assignment\UDP_" + filename + ".txt"

with open(path, "wb") as f:
    bytes_data = sock.recv(buf_size[0])
    while(True):
        f.write(bytes_data)  
        bytes_data = sock.recv(buf_size[0])
        if not bytes_data:
            break
    
sock.close()
end = time.time()
print(end - start)






# for i in range(filesize//buf_size[0]):
#         f.write(bytes_data)
#     try:
#         f.write(sock.recv(filesize%buf_size[0]))            
#     except:
#         print("error(Timeout), Packet loss")
    