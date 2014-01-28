#!env/bin/python

import sys

def palindrom(num):
  l = len(str(num))
  m = l / 2
  if l & 1:
    return False
  elif str(num)[0:m] == str(num)[m:l][::-1]:
    return True
  else:
    return False

nbrs = range(1000,100,-1)
#nbrs = range(10,100,1)
result = 0
for x1 in nbrs:
  for x2 in nbrs:
    sys.stdout.write('\r')
    if palindrom(x1*x2):
      if x1*x2 > result:
        print str(x1)+"*"+str(x2)+"="+str(x1*x2)
        result = x1*x2

print result

