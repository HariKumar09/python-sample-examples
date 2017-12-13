import os
import subprocess

#
# import os
# os.system('command')
#
# f = open('text.txt', 'r')
# b = f.readline()
# while b:
#     cmd = 'grep %s my2.txt' % b
#     # my2 is the file in which we are looking for b
#     os.system(cmd)
#     b = f.readline()
# f.close()
#
# a = 'He is'
# cmd = 'grep %s my2.txt' % a
# os.system(cmd)


def grep_lines(filename, query_filename):
    with open(query_filename, "rb") as myfile:
        for line in myfile:
            subprocess.call(["/bin/grep", line.strip(), filename])
            grep_lines("text.txt", "my2.txt")
