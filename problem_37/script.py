#!env/bin/python

import helpers as h

c = 0
x = 23
r = 0

while c < 11:
    while not h.is_prime(x):
        x += 2
    for ch in str(x):
        if int(ch) % 2 == 0 and ch != '2':
            x += 2
    number = x
    skip = False
    while number > 0:
        if not h.is_prime(number):
            skip = True
            break
        number /= 10
    if skip:
        x += 2
        continue
    number = x % (10**int(h.log10(x)))
    while number > 0:
        if not h.is_prime(number):
            skip = True
            break
        number = number % (10**int(h.log10(number)))
    if skip:
        x += 2
    else:
        c += 1
        print x
        r += x
        x += 2
print r
