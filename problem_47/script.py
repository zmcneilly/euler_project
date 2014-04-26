#!env/bin/python

import helpers as h

MAX = 200000
pdict = h.find_primes(MAX)
plist = []
for p in pdict:
    if pdict[p]:
        plist.append(p)
plist.sort()
pset = set(plist)

c = 1

for x in xrange(210,MAX):
    if len(h.distinct_prime_factors(x,pset)) >= 4:
        c += 1
    else:
        c = 0
    if c >= 4:
        break

print x -3
