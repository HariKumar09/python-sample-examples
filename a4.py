import os

f = open('text.txt', 'r')
b = f.readline()
while b:
    cmd = 'grep %s my2.txt' % b
    # my2 is the file in which we are looking for b
    os.system(cmd)
    b = f.readline()
f.close()

a = 'He is'
cmd = 'grep %s my2.txt' % a
os.system(cmd)
