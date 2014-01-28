#!env/bin/python

import sys

factors=[11,12,13,14,15,16,17,18,19,20]
l = len(factors)
x = factors[l-1]
fin = False
while not fin:
  fac = True
  for x1 in factors:
    if x % x1 != 0:
      x += factors[l-1]
      fac = False
      break
  if fac:
    fin = True
print x
