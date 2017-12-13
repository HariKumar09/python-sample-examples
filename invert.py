def invertDictionary(d):
   myDict = {}
   for i in d:
       value = d.get(i)
       myDict.setdefault(value,[]).append(i)
       return myDict
print invertDictionary({'x': 1, 'y': 2, 'z': 3})
