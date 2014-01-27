#!env/bin/python

nbr = 600851475143
#nbr = 13195
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

def factors(num):
  MAX = num/2
  x = 2
  result=[]
  while x < MAX:
    if num % x == 0:
      for x1 in (factors(num/x)):
        if x1 not in result:
          result.append(x1)
      if x not in result:
        result.append(x)
    x += 1
  return result

result = 1
to_check=factors(nbr)
print "Done Factoring"
for x in to_check:
  if isprime(x) and x > 0:
    if nbr % x == 0 and x > result:
      result = x

print result
