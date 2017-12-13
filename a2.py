f = open("text.txt", "rb")
s = f.readlines()
f.close()
f = open("newtext.txt", "wb")
s.reverse()
for item in s:
    print f, item
f.close()
