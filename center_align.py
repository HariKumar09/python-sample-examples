import sys


def center_alignment(filename):
	f = open("she.txt").readlines()
	x = len(max(f))
	for line in f:
		p = (x-len(line))/2
		print ' '*p+line
		center_alignment(sys.argv[1])
