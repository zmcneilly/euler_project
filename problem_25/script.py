#!env/bin/python

import helpers as h
import sys

goal=1000
step=100000
p = 0
f1 = h.fibonacci_r(step)
f0 = h.fibonacci_r(step-1)

while h.num_digits(f1) > goal:
    step = (step+p)/2
    f1 = h.fibonacci_r(step)

while h.num_digits(f1) < goal:
    step =step+1
    f1 = h.fibonacci_r(step)

print 'n: '+str(step)+'\tF: '+str(f1)
