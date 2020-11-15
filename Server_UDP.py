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

def thread(connection,address): 
    path= r"D:\Networks Assignment"
    filename= connection.recvfrom(50)[0].decode()
    print(filename)
    path = path +"\\" +filename + ".txt"
    filesize = os.path.getsize(path)
    
    connection.sendto(f"{filename}{sep}{filesize}".encode(),address)  
    print("recieved")
    # progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(path, "rb") as f:
        # for _ in progress:
        while(True):
            bytes_read = f.read(buf_size[0])
            connection.sendto(bytes_read,address)
            if not bytes_read:
                connection.sendto(bytes_read,address)
                break
            time.sleep(.0001)
        connection.sendto(b'', address)
    f.close()

socke = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socke.bind((host,port))   

print("Binding Cmplete, Listning at 12345") 
while(True):
    connection, address =socke.recvfrom(2)
    print(connection)
    print(address)
    print("Connection succesful")
    threading.Thread(target=thread, args=(socke, address,)).start()






