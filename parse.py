# import csv
# # res=[]
#
#
# def parse_csv(file):
#     f = open(a.csv, 'r')
#     txt = f.readlines()
#     for l in txt:
#         s = re.findall('\w+', l)
#         res.append(s)
#         print res
#         parse_csv('a.csv')


import csv
import parser

reader = csv.reader(['a!b!c', '1!2!3', '2!3!4', '3!4!5"'],
                    skipinitialspace=True)

for r in reader:
    print r
