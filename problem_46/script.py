#!env/bin/python

import helpers as h

MAX = 10000

pdict = h.find_primes(MAX)
plist = []

for x in pdict:
    if pdict[x]:
        plist.append(x)

pset = set(plist)

def goldbach_other(n):
    for a in plist:
        if a >= n:
            return False
        for b in xrange(1,n):
            if n == (a + 2 * b * b):
                return True

for x in xrange(33,MAX,2):
    if pdict[x]:
        continue
    if not goldbach_other(x):
        print x
        MAX = 0


