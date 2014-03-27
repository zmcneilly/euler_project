#!env/bin/python

import helpers as h
print 2
for x in range(3,1000001,2):
    skip = False
    for c in str(x):
        if int(c) % 2 == 0:
            skip = True
            break
    if skip:
        continue
    if h.is_circular_prime(x):
        print x
