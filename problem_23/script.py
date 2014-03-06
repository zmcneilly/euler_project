#!env/bin/python

import helpers as h

an = {}
x = 12
MAX = 28123
while x <=  (MAX/2):
    if h.is_abundant(x):
        an[x] = True
    x += 1
print "Factored!"
sums = {}
for n in range(13,MAX+1,1):
    sums[n] = False
print "Generated sums"
for n1 in an:
    for n2 in an:
        if n2 > n1:
            sums[n1+n2] = True
print "Generated total"

result = 0
for n in sums:
    if not sums[n]:
        result += n

print result
