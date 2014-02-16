#!env/bin/python

import helpers as h

result = {}
for x in range(1,10001,1):
    result[x]=-1

for x in result:
    if result[x] == -1:
        result[x] = h.is_amicable(x)
        if result[x] < 10000 and result[x] > 0:
            result[result[x]] = x

total = 0
for x in result:
    if result[x]> -1:
        print x
        total += x

print total
