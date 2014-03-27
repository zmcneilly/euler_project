#!env/bin/python

import helpers as h

fn = {}
for x in range(0,10):
    fn[x] = h.factorial(x)

print fn

def check(n):
    s = str(n)
    for x in range(6,10):
        if str(x) in s:
            return False
    return True
def sofd(n):
    res = 0
    for c in str(n):
        res += fn[int(c)]
    return res

x = 3

p = 9
MAX = fn[9]

while p < MAX:
    p = (p*10)+9
    MAX += fn[9]

print sofd(33306)

while x <= MAX:
    sumOfFacts = 0
    number = x
    while number > 0:
        sumOfFacts += fn[number%10]
        number /= 10
    if sumOfFacts == x:
        print x
    x += 1
