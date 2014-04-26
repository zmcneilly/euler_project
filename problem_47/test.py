from helpers import *

pdict = find_primes(200000)
plist = []
for p in pdict:
  if pdict[p]:
    plist.append(p)
plist.sort()
pset = set(plist)
