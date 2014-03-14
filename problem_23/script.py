#!env/bin/python

import helpers as h

an = {}
x = 1
MAX = 28123
while x <=  (MAX):
    if h.is_abundant(x):
        an[x] = True
    x += 1

keys = an.keys()

print "Factored!"
sums = {}
for n in range(2,MAX+1,1):
    sums[n] = False
print "Generated sums"
result = 1 
for n in reversed(keys):
    for x in an:
        if n+x > MAX:
            break
        if x <= n:
            sums[n+x] = True
        else:
            break

for n in sums:
    if not sums[n]:
        result+=n

print result
