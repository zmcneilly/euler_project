#!env/bin/python
from math import sqrt
collatz_cache = {}

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

def is_prime(n):
    if n in find_primes(n):
        return True
    else:
        return False

def find_primes(MAX):
    result = 0
    primes = {}

    for x in xrange(2,MAX+1,1):
      primes[x] = True

    for i in range(2,int(math.sqrt(MAX))+1,1):
      if primes[i]:
        for j in range(i*i,MAX+1,i):
          primes[j] = False

    for x in primes:
      if primes[x]:
        result += x

    return result

def collatz_seq(n):
    result = []
    if n == 1:
        result.append(1)
    elif n % 2 == 0:
        result.append(n)
        result.extend(collatz_seq(n/2))
    else:
        result.append(n)
        n1 = (3*n)+1
        result.append(n1)
        result.extend(collatz_seq((n1)/2))
    return result

def collatz_cnt(n):
    if n in collatz_cache:
        return collatz_cache[n]
    if n == 1:
        collatz_cache[n] = 1
    elif n % 2 == 0:
        collatz_cache[n] = 1+collatz_cnt(n/2)
    else:
        collatz_cache[n] = 1+collatz_cnt(3*n+1)
    return collatz_cache[n]

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def n_choose_r(n,r):
    """How many combinations with r items can be made from the n given items"""
    return factorial(n)/(factorial(r)*factorial(n-r))

def sum_of_digits(n):
    """Return the sum of the digits of the number"""
    o = str(n)
    result = 0
    for x in o:
        result += int(x)
    return result

def sum_of_divisors(n):
    result = 0
    for x in find_factors(n):
        if x < n:
            result += x
    return result

def is_amicable(n):
    result = -1
    dn = sum_of_divisors(n)
    dn1 = sum_of_divisors(dn)
    if n == dn1 and dn != dn1:
        result = dn
    return result

def alphabetic_value(name):
    lname = name.lower()
    result = 0
    for char in lname:
        result += ord(char) - 96
    return result

