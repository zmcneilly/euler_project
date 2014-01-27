#!env/bin/python

nbr = 600851475143
primes=[]

def isprime(num):
  if num == 0 or num == 1:
    return True
  for x in primes:
    if num % x == 0:
      return False
  if num in primes:
    return True
  else:
    primes.append(num)
    return True

result = 1
MAX = nbr/2
x = 1
while x <= MAX:
  x += 1
  if isprime(x) and x > 0:
    if nbr % x == 0:
      result = x

print result
