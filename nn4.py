def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)


import md5
 m = md5.new()
 m.update("Nobody inspects")
 m.update(" the spammish repetition")
 m.digest()


def get_md5(filename, block_size=2 ** 20):
    """Returns an MD5 hash for a filename."""
    f = open(filename, 'rb')
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()




import hashlib

def md5(text):
	"""Returns the md5 hash of a string."""

	hash = hashlib.md5()
	hash.update(_string(text))

	return hash.hexdigest()



import hashlib

email = "aaaaaaa"
storage_path = "C:\Users\pandu\Downloads\simple-websocket-server-master.zip"
def get_md5(self, storage_path):

    get_md5 = hashlib.md5()
    get_md5.updateupdate(''.join([self.email, ':', storage_path]))

    return get_md5.hexdigest()

print _generate_metadata_hash(email, storage_path)




def _generate_metadata_hash(email, storage_path):
    # Generate an application specific hash of the file metadata.
    md = hashlib.md5()
    md.update(''.join([email, ':', storage_path]))
    return md.hexdigest()



import hashlib

email = "aaaaaaa"
storage_path = "C:\Users\pandu\Downloads\simple-websocket-server-master.zip"
def _generate_metadata_hash(email, storage_path):
    # Generate an application specific hash of the file metadata.
    md = hashlib.md5()
    md.update(''.join([email, ':', storage_path]))
    return md.hexdigest()
print _generate_metadata_hash(email, storage_path)




import socket
import time

HOST = "localhost"
PORT = 5454
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST,PORT))
while True:

      data = raw_input("Enter..... ")
      s.sendto(data,(HOST,PORT))

      print "Server says: " + s.recv(1024)

      if data=="bye" or s.recv(1024)=="bye":
           print "Exiting..........."
           time.sleep()
           break


from socket import *

host = "127.168.2.75"
port = 4446

s=socket(AF_INET, SOCK_STREAM)
s.bind((host,port))

s.listen(1)

print "Listening for connections.. "
q,addr=s.accept()

data=raw_input("Enter data to be send: ")
q.send(data)





import socket
import time

HOST = "localhost"
PORT = 5454
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST,PORT))
while True:

      print "Client says: " + s.recv(1024)

      data = raw_input("Enter..... ")
      s.sendto(data,(HOST, PORT))

      if data=="bye" or s.recv(1024)=="bye":
           print "Exiting.................."
           time.sleep()
           break


from socket import *

host = "127.168.2.75"
port = 4446

s=socket(AF_INET, SOCK_STREAM)
s.connect((host,port))
msg=s.recv(1024)
print ("Message from client: " + msg.strip().decode('ascii'))
