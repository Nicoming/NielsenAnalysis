'''''''''''
#merge title id according to names.unique
nielsen <- nielsen[order(nielsen$names.unique, nielsen$title_id_use),]
b = 2
repeat {
  if (nielsen$names.unique[b-1] == nielsen$names.unique[b]){nielsen$title_id_use[b] = nielsen$title_id_use[b-1]}
  b=b+1
  if (b == length(nielsen$names.unique)) break}


#same author function
#if the author at position [n] contains the sting in position [n-1], author[n] = author[n-1]

SameAuthor = function(author){if isTRUE(author[n-1] %in% author[n])}{author[n] = author[n-1]}

save it as CombinedCuration2.csv


def make_unicode(c):
    if type(c) != str:
        c = c.decode('utf-8')
        return c
    else:
        return c
'''
'''''''''
def unicode_csv_reader(utf8_data,dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data,dialect=dialect,**kwargs)
    for row in csv_reader:
        print(type(row[2]))
        if type(row[2])==str:
            yield [cell.encode('utf-8') for cell in row]
        else:
            yield [cell.decode('utf-8').encode('utf-8') for cell in row]

        try:
            yield [cell.encode('utf-8') for cell in row]
            print('No catch')
        except UnicodeError as e:
            print('Caught')
            print(e)
            yield [cell.decode('utf-8').encode('utf-8') for cell in row]
            continue

'''''''''
filename = 'CombinedCurationO.csv'
data=[]
import csv
with open(filename,newline='') as f:
    reader = csv.reader(f)
    for i in range(308560):
        print(i)
        try:
            row = next(reader)
            for cell in row:
                cell.encode('ascii')
            row = next(reader)
            print(row)
        except UnicodeDecodeError as e:
            print('caught')
            print(e)
            print(row)

            for cell in row:
                cell.encode('utf-8')
            print('continued')
            continue
#reader = unicode_csv_reader(open(filename))
#for i in reader:
#    print(i)
#import pandas as pd
#reader = csv.reader(open('CombinedCuration.csv'))
import sys
#myD = []
#try:
#    for line in open('CombinedCuration.csv',"r"):
#        myD.append(line.strip())
#except UnicodeError:
#        myD.append(line.encode('utf-8'))
#        continue
#myD = pd.read_csv('CombinedCuration.csv')
#while True:

#else:
#        pass
#for line in open('CombinedCuration.csv'):
#    try:
#        myD.append(line.strip())
#    except UnicodeError:
#        myD.append(line.encode('utf-8'))
print(len(myD))
#for i in range(10):
 #   print(i)
  #  print(myD[i])
for i in range(85280,85293):
    print(i)
    print(myD[i])
#len(myD)
    #line = line.decode('windows-1252')
    #try:
    #myD.append(make_unicode(line))
    #except UnicodeDecodeErroreError:
     #   myD.append(make_unicode(line))
    #else:
     #   pass
    #try:
     #   myD.append(line.encode('ascii'))
    #except UnicodeError:
        #myD.append(line.encode('utf-8'))
    #else:
     #   pass
#myD = [line.encode('utf-8').strip() for line in open('CombinedCuration.csv').readlines()]