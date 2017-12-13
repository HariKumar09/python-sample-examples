# from collections import OrderedDict
# from operator import itemgetter
# data = valuesort({'x': 1, 'y': 2, 'a': 3})
# d = OrderedDict(sorted(data.items(), key=itemgetter(1)))
# d.values()
# print d


myDictionary = {'x': 1, 'y': 2, 'a': 3}

newDictionary={}

sortedList=sorted(myDictionary.values())

for sortedKey in sortedList:
    for key, value in myDictionary.items():
        if value==sortedKey:
            newDictionary[key]=value
            print newDictionary
