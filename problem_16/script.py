#!env/bin/python

import helpers as zf
import structures as zs
import math,decimal

x = decimal.Decimal(math.pow(2,1000))
result = 0
decimal.getcontext().prec=302
while(x > 0):
    decimal.getcontext().prec=302
    xs = str(x)
    print xs
    result += int(xs[0])
    if xs.find('E') > -1:
        x = decimal.Decimal(x - decimal.Decimal(xs[0]+xs[xs.find('E'):]))
    else:
        x = decimal.Decimal(x - decimal.Decimal(xs[0]+'e'+str(len(xs)-1)))
    print result

print "Result:"
print result
