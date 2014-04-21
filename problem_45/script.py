#!env/bin/python

import helpers as h
from math import sqrt

done = False
n = 144

while not done:
    hn = h.hexagonal_num(n)
    if h.test_pentagonal_num(hn):
        done = True
        t = (sqrt(8*hn+1)-1)/2
        print "T({}) = {}".format(t,hn)
    else:
        n += 1
