#!env/bin/python

i = 1
t = 3
primes = [2]

while i < 10002:
  p = True
  for x in primes:
    if t % x == 0:
      p = False
      break
  if p:
    primes.append(t)
    i += 1
  t += 2

print primes[len(primes)-10:]
