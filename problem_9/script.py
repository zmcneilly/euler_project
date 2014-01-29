#!env/bin/python

import sys

sresult = 1000

s1 = range(1,1000,1)
s2 = range(1,1000,1)
s3 = range(1,1000,1)
sqs = []

def test1(a,b,c):
  if (a + b + c) == 1000:
    return True
  else:
    return False

def test2(a,b,c):
  if ((a*a)+(b*b)) == (c*c):
    return True
  else:
    return False

for a in s1:
  s2 = range(a+1,1000,1)
  for b in s2:
    s3 = range(b+1,1000,1)
    for c in s3:
      if test1(a,b,c):
        if test2(a,b,c):
          sys.stdout.write('\n')
          print "Solution:"
          print "A: "+str(a)
          print "B: "+str(b)
          print "C: "+str(c)
          sys.exit(0)
        else:
          sys.stdout.write('\r')
          sys.stdout.write('A:\t'+str(a)+'\tB:\t'+str(b)+'\tC:\t'+str(c))
          sys.stdout.flush
