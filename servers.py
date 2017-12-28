import socket
import sys

host = 'localhost'
port = 61473
address = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(1)

print "Listening for client . . ."
conn, address = server_socket.accept()
print "Connected to client at ", address

while True:
    output = conn.recv(2048);
    if output:
        print "Message received from client:"
        print output
        conn.send("ack")
