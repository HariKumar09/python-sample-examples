import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 61473))

data=raw_input("Enter data to be send: ")
print 'send to server: ' + data
client_socket.send(data)

while client_socket.recv(2048) != "ack":
    print "waiting for ack"
print "ack received!"

client_socket.close()
