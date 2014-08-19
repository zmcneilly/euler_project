#!env/bin/python

import helpers as h

count = 0

for __n in xrange(2,10001):
    if h.sqrt(__n) == h.floor(h.sqrt(__n)):
        continue
    a0, seq = h.continued_fraction_expansion(__n)
    len_seq = len(seq)
    if len_seq == 1 or len_seq % 2 == 1:
        count += 1

print count


