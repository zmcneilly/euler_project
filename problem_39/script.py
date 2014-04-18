#!env/bin/python

import helpers as h
import math

r = {}

for x in range(1000,0,-1):
    if not h.is_square(x): continue
    r[x] = 0
    MAX = int(math.sqrt(x))
    for a in range(1,MAX):
        for b in range(1,MAX):
            if a + b + math.sqrt(a*a+b*b) == x:
                print "i={} a={} b={} c={}".format(i,a,b,i-a-b)
                r[x]+=1

