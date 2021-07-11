#UDP client
import socket
HOST = 'localhost'
PORT = 9999

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg = "hello, from client"
client.sendto(msg.encode('utf-8'),(HOST,PORT))
data, addr = client.recvfrom(4096)
print(data.decode('utf-8'))

while True:
    msg = input("Enter Message:")
    client.sendto(msg.encode('utf-8'),(HOST,PORT))
# client.close()