#!env/bin/python

import sys,math

result = 0
MAX = 2000000
#MAX = 10
primes = {}

for x in range(2,MAX+1,1):
  primes[x] = True

for i in range(2,int(math.sqrt(MAX))+1,1):
  if primes[i]:
    for j in range(i*i,MAX+1,i):
      primes[j] = False

for x in primes:
  if primes[x]:
    result += x

print result
