#!env/bin/python
from math import sqrt

def triangle_num(n):
  i = 0;
  result = 0;
  while i <= n:
    result += i
    i += 1
  return result

def find_factors(n):
  factors=[]
  MAX = int(sqrt(n))+1
  for i in range(1,MAX,1):
    if n % i == 0:
      factors.append(i)
      factors.append(n/i)
  return factors

def find_primes(MAX)
    result = 0
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

    return result
