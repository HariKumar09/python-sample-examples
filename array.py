Matrix[0][0] = 1
Matrix[6][0] = 3
# error! range...
Matrix[0][6] = 3
# valid

print Matrix[0][0]
# prints 1
x, y = 0, 6
print Matrix[x][y]
# prints 3; be careful with indexing! 
