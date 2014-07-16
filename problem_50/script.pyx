#!env/bin/python
#
#The prime 41, can be written as the sum of six consecutive primes:
#
#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below
#one-hundred.
#
#The longest sum of consecutive primes below one-thousand that adds to a prime,
#contains 21 terms, and is equal to 953.
#
#Which prime, below one-million, can be written as the sum of the most
#consecutive primes?
#

import pyximport; pyximport.install()
import helpers as h

def main():
    MAX = 1000000
    pdict = h.find_primes(MAX)
    plist = []
    for p in pdict:
        if pdict[p]:
            plist.append(p)
    pset = set(plist)
    plist.sort()

    l = len(plist)/50
    done = False

    while not done:
        for x in xrange(0,len(plist)-l+1):
            l1 = plist[x:x+l]
            t = sum(l1)
            if t in pset:
                print t
                done = True
                break
            if t > MAX:
                break
        l -= 1

if __name__ == '__main__':
    main()
