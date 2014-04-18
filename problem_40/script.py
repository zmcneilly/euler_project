#!env/bin/python

MAX = 1000000
s = ''

for x in range(1,MAX+1):
    s = s+str(x)

# d1  d10  d100  d1000  d10000  d100000  d1000000

t = 1

for x in (1,10,100,1000,10000,100000,1000000):
    t = t * int(s[x-1])

print t
