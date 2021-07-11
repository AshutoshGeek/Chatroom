#UDP client
import socket

HOST = 'localhost'
PORT = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))

while True:
    data, addr = s.recvfrom(4096)
    print(data.decode('utf-8'))
    message = "Hello, from udp server"
    s.sendto(bytes(message,'utf-8'),addr)