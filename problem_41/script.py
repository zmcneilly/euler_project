#!env/bin/python

import helpers as h

def list_to_num(n):
    s = ''
    for x in n:
        s = s + str(x)
    return int(s)

result = None
s = [10,9,8,7,6,5,4,3,2,1]
while result == None:
    s.pop(0)
    t = 0
    for x in s:
        t += x
    if t % 3 == 0:
        continue
    for x in h.permute(s):
        if x[len(s)-1] % 2 == 0:
            continue
        if h.is_prime(list_to_num(x)):
            result = x
            break
    print s

print result
