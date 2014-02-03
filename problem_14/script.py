#!env/bin/python

import sys,helpers

result = 0
MAX=0
n = 1
while n < 1000000:
    c = helpers.collatz_cnt(n)
    if c > MAX:
        result = n
        MAX = c
        print result
    n += 2
