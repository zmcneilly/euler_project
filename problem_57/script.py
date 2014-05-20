#!env/bin/python

import fractions

f = fractions.Fraction(3,2)
c = 0

for x in xrange(0,1000):
    d = f.denominator
    n = f.numerator
    if len(str(d)) < len(str(n)):
        c += 1
    d1 = (d+n)
    n1 = (d1+d)
    f = fractions.Fraction(n1,d1)
    
print c
