#TCP CLIENT
import socket
HOST = '127.0.0.1'
PORT = 9999
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

# payload= "Hello world!"
# data = client.recv(1024)
# print(data.decode('utf-8'))
con = 1
while con:
    payload = input("Enter payload: ")
    client.send(payload.encode(FORMAT))
    if payload.lower() == "exit":
        con = 0
client.close()