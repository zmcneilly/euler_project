#!env/bin/python
#
#By replacing the 1st digit of the 2-digit number *3, it turns out that six of
#the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
#By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
#number is the first example having seven primes among the ten generated
#numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
#56993. Consequently 56003, being the first member of this family, is the
#smallest prime with this property.
#
#Find the smallest prime which, by replacing part of the number (not necessarily
#adjacent digits) with the same digit, is part of an eight prime value family.

import helpers as h
import sys

def commonality(n1,n2):
    s1 = str(n1)
    s2 = str(n2)
    r = ''
    if len(s1) != len(s2):
        return ('',-1)
    for x in xrange(0,len(s1)):
        if s1[x] == s2[x]:
            r = r + s1[x]
        else:
            r = r + '*'
    return r

def prime_matches(pat,pset):
    count = 0
    matches = []
    for digit in xrange(0,10):
        r = int(pat.replace('*',str(digit)))
        if r % 2 == 0:
            break
        if str(r) != pat and r in pset:
            count += 1
            matches.append(r)
    return (matches,count)

count = 0
best = ''
MAX = 1000000
MIN = 100000
pdict = h.find_primes(MAX)
plist = []
for p in pdict:
    if pdict[p] and p >= MIN:
        plist.append(p)
pset = set(plist)
plist.sort()

p = 3
while True:
    for mask in h.nCr(xrange(0,6),p):
        for prime in plist:
            prl = list(str(prime))
            for x in mask:
                prl[int(x)] = '*'
            r = prime_matches(''.join(prl),pset)
            if r[1] >= 8:
                print r[0]
                sys.exit()
    p -= 1
