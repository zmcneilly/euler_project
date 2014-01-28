#!env/bin/python

nbrs = range(1,101,1)
tot = 0
sqs = 0
for x in nbrs:
  tot += x
  sqs += (x*x)
totsq = tot * tot
print totsq-sqs
