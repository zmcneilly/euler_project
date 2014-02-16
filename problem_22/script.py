#!env/bin/python

import helpers as h

f = open('names.txt','r')
names = f.read().split('","')
i = 0
while i < len(names):
    names[i] = names[i].strip('"')
    i+=1

names.sort()
i = 1
result = 0

for name in names:
    result += i * h.alphabetic_value(name)
    i += 1

print result
