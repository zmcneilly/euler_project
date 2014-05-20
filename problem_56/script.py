#!env/bin/python

import helpers as h

best = 0

for a in xrange(1,100):
    for b in xrange(1,100):
        ab = list(str(a**b))
        total = 0
        for x in ab:
            total += int(x)
        if total > best:
            best = total

print best

