#!env/bin/python
from math import sqrt,floor,log10
import decimal
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

def is_abundant(n):
    result = 1
    MAX = int(sqrt(n))
    for i in range(2,MAX+1,1):
      if n % i == 0:
        result+=i
        if i != (n/i):
            result+=(n/i)
        if result > n:
            return True
    return False

def o_is_abundant(n):
    result = 0
    for x in set(find_factors(n)):
        if x < n:
            result += x
    if result > n:
        return True
    else:
        return False 

def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs,low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]

def zmute(s, goal):
    if len(s) == 1:
        return s[0]
    elif goal == 1:
        result = ''
        for x in s:
            result = result+str(x)
        return result
    else:
        steps = factorial(len(s)-1)
        if goal >= steps:
            pos = ((goal-1) / steps)
            goal = goal - (steps*pos)
        else:
            pos = 0
        s0 = s[pos]
        s1 = []
        for x in s:
            if x != s0:
                s1.append(x)
        return str(s0)+str(zmute(s1,goal))


def fibonacci_r(n):
    """This is an implementation of Wikipedia's formula for estimating a
    Fibonacci number at index 'n' through use of rounding"""
    phi = (1 + sqrt(5))/2
    if n >= 0:
        return \
        ((pow(decimal.Decimal(phi),decimal.Decimal(n))/decimal.Decimal(sqrt(5)))+\
        decimal.Decimal(.5)).to_integral_exact(rounding=decimal.ROUND_FLOOR)
    else:
        return 0

def num_digits(n):
    """This function is intended to return the number of digits of n"""
    d = decimal.Decimal(n)
    l = d.log10().to_integral_exact(rounding=decimal.ROUND_FLOOR)
    return l + 1
