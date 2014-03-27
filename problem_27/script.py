#!env/bin/python

import helpers as h

MAX = 1000
bl = -1
ba = 0
bb = 0
br = -1
for a in range(-1*MAX,MAX+1):
    for b in range(-1*MAX+1,MAX+1,2):
        if not h.is_prime(b):
            continue
        i = 0
        r = (i*i)+(a*i)+b
        pr = 0
        while h.is_prime(r):
            i += 1
            r = (i*i)+(a*i)+b
        if i >= bl:
            bl = i
            ba = a
            bb = b

print 'n = 0 to '+str(bl)
print 'a = '+str(ba)
print 'b = '+str(bb)
