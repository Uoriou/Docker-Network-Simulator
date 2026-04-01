import socket 

s = socket.socket()
s.connect(('192.168.100.2', 9999))  
print("Connected")