#!env/bin/python

import sys

nbr = 600851475143

def uniq(sortedlist):
  result = [sortedlist[0]]
  x = 3
  while x < len(sortedlist):
    if sortedlist[x-1] < sortedlist[x]:
      result.append(sortedlist[x])
    x += 1
  return result

def factors(num):
  x = 2
  MAX = num / 2
  result = []
  while num % x != 0 and x < MAX:
    x += 1
    if x % 1000000 == 0 or x < 1000000:
      sys.stdout.write('\r')
      sys.stdout.write("X: "+str(x))
      sys.stdout.flush()
  if x >= MAX:
    return num
  else:
    sys.stdout.write('\r')
    print "Factor: "+str(x)+", "+str(num/x)
    calc = factors(num/x)
    if type(calc) == type([]):
      result.extend(calc)
    else:
      result.append(calc)
    return result

result = factors(nbr)
result.sort()
print uniq(result)
