import socket

s = socket.socket()
s.bind(('192.168.100.2', 9999))
s.listen(1)
print("Waiting for connection...")
conn, addr = s.accept()
print(f"Connected from {addr}")