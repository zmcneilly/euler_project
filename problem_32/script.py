#!env/bin/python

import helpers as h
import time,sys
p = [1,2,3,4,5,6,7,8,9]
res = []
for x in h.permute(p):
    l, r, s = '', '', ''
    for c in x[0:2]: l += str(c)
    for c in x[2:5]: r += str(c)
    for c in x[5:]: s += str(c)
    a = int(l)*int(r)
    if int(s) == a:
        print x
        res.append(a)
    l, r, s = '', '', ''
    for c in x[0:1]: l += str(c)
    for c in x[1:5]: r += str(c)
    for c in x[5:]: s += str(c)
    a = int(l)*int(r)
    if int(s) == a:
        print x
        res.append(a)

r = 0
for x in set(res):
    r += x
print set(res)
print r
