#!env/bin/python

#There are exactly ten ways of selecting three from five, 12345:
#
#123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
#In combinatorics, we use the notation, 5C3 = 10.
#
#In general,
#
#
#It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#
#greater than one-million?

import helpers as h

count = 0

for n in xrange(1,101):
    for r in xrange(1,n+1):
        if h.n_choose_r(n,r) >= 1000000:
            count += 1

print count
