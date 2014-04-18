#!env/bin/python

import helpers as h

MAX = 0
lines = open('./words.txt').read().split(',')
tns = []
result = 0

for line in lines:
    s = 0
    for c in line.lower().strip('"'):
        s += ord(c)-96

    if s > MAX:
        for x in xrange(MAX+1,s+1):
            tns.append(h.triangle_num(x))
        MAX = s
    if s in tns:
        result += 1

print result


