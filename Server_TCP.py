# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket
import sys
import os
import tqdm
import threading
import time

sep = "<$$$$$>"

buf_size = [1024]

host = socket.gethostname()
port = 12345
nagle = False

delay = True 



def thread(connection,address): 
    path= r"D:\\Networks Assignment"
    
    filename= connection.recv(32).decode()
    path = path +"\\" +filename + ".txt"
    filesize = os.path.getsize(path)
    print(path)
    connection.send(f"{filename}{sep}{filesize}".encode()) 
    print("recieved")
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(path, "rb") as f:
        for _ in progress:
            bytes_read = f.read(buf_size[0])
            if not bytes_read:
                break
            connection.sendall(bytes_read)
            progress.update(len(bytes_read))
            time.sleep(.0001)
    connection.close()

socke = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if(not nagle):
    socke.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
    
if not delay:
       socke.setsockopt(socket.SOL_TCP, socket.TCP_QUICKACK, False)
socke.bind((host,port))   
socke.listen()
print("Binding Cmplete, Listning at 12345")
while(True):
    connection, address =socke.accept()
    print("Connection succesful")
    threading.Thread(target=thread, args=(connection, address,)).start()






