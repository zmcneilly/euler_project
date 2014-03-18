#!env/bin/python
#IDEA: Two arrays, when one matches the other we have a pattern

from decimal import *

# MAX is the highest denominator we are going to check
MAX = 1000
# L is the number of decimal points of precision to use
# The local maximum for the number of repeated decimal places appears to be 2 *
# the denominator. I.e. for numbers less than 1000, all cycles will be less
# than 1000 digits, for numbers less than 100 all cycles will be less than 100
# digits, etc.
L=2*MAX
getcontext().prec=L
lg = '0'
ln = 0
ls = '0'
# We start high because it's easy to tell early if a number is too short to be
# a valid possibility, and it's likely to be a large number.
for n in range(MAX,2,-1):
    # Create the string we are parsing
    s = str(1/Decimal(n))[2:]
    l = len(s)
    sm = ''
    # If the number of digits after the decimal is less than the current max,
    # don't bother testing. This shaves about 75% of the time off this
    # algorithm.
    if l < len(ls):
        break
    # Starting at pos 0, we want to compare every possible string of
    # consecutive digits, of length starting at 1/2 of the full length and
    # going on until a length of 2. This method ensures we find the shortest
    # pattern for a particular string. I.e. '14141414' should have a cycle of
    # '14', not '141' or '1414'.
    for nc in range(l/2,1,-1):
        for p in range(0,l-nc,nc):
            s1 = s[p:nc]
            s2 = s[nc:2*nc]
            if s1 == s2:
                sm = s1
    if len(sm) > len(lg):
        lg = sm
        ln = n
        ls = s

print 'N:\t1/'+str(ln)+'\tR:\t'+ls+'\tL:\t'+str(len(lg))
