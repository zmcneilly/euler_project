#!env/bin/python

from helpers import *

def lychrel_num(n,m):
    """Returns True if n doesn't generate a palindrome within m iterations"""
    np = int(str(n)[::-1])
    if is_palindrome(n + np):
        return False
    elif m <= 0:
        return True
    else:
        return lychrel_num(n+np,m - 1)

c = 0
for x in xrange(10,10000):
    if lychrel_num(x,50):
        c += 1

print c

