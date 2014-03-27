#!env/bin/python

import helpers as h
res = 0
for x in range(1,1000000,2):
    if h.is_palindrome(x):
        if h.is_palindrome(h.str_base(x,2)):
            print "B10: {}\tB2: {}".format(x,h.str_base(x,2))
            res += x
print res
