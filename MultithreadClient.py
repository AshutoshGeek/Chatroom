import socket

HEADER = 64
PORT = 5555
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

username = input(print("Enter a Username:"))
send(f"Hello from {username}!")
con = 1
while con:
    # send("Hello from client!")
    payload = input("Enter payload: ")
    send(payload)
    if payload.lower() == "exit":
        con = 0

send(DISCONNECT_MESSAGE)