#!env/bin/python


#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
#by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
#(ii) each of the 4-digit numbers are permutations of one another.
#
#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
#exhibiting this property, but there is one other 4-digit increasing sequence.
#
#What 12-digit number do you form by concatenating the three terms in this
#sequence?

import helpers as h

def num_to_list(n):
    s = str(n)
    r = []
    for c in s:
        r.append(int(c))
    return r

def list_to_num(l):
    r = ''
    for i in l:
        r = r + str(i)
    return int(r)

pdict = h.find_primes(10000)
plist = []
for p in pdict:
    if pdict[p]:
        plist.append(p)
pset = set(plist)
plist.sort()

canidates = []

for p in plist:
    if p > 999:
        canidates.append(num_to_list(p))

permutes = []
for canidate in canidates:
    cc = 0
    p = []
    for t in h.permute(canidate):
        ti = list_to_num(t)
        if ti < 999:
            continue
        if ti in pset:
            cc += 1
            p.append(ti)
    if cc >= 3:
        permutes.append(list(set(p)))

for p in permutes:
    p.sort()
    if 1487 in p:
        print 'hello'
    for x in xrange(0,len(p)-2):
        for y in xrange(x+1,len(p)-1):
            for z in xrange(y+1,len(p)):
                if p[z] - p[y] == p[y] - p[x]:
                    print "{} -> {} -> {}".format(p[x],p[y],p[z])

