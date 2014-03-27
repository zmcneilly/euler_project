#!env/bin/python

import helpers as h

result = 0
for x in range(10,2540162):
    sumOfFacts = 0
    number = x
    while (number > 0):
        d = number % 10
        number /= 10
        sumOfFacts += h.factorial(d)
    if sumOfFacts == x:
        print x
