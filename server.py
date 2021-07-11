#TCP server
import socket, sys

HOST = '127.0.0.1'
PORT = 9999
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("socket created")
except socket.error as err:
    print("failed to create a socket")
    print("Reason "+ str(err))
    sys.exit()

s.bind((HOST,PORT))
print("socket bind to %s" % PORT)

s.listen(5)
print("socket is listening")

while True:
    c , addr = s.accept()
    print("connection from", addr)
    c.send(bytes("Hello, This is from server.",'utf-8'))

    while True:
        data = c.recv(1024)
        if not data or data.decode('utf-8')=='END':
            break
        print('recieved from client: %s' % data.decode('utf-8'))
    c.close()