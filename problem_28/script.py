#!env/bin/python

s = 1
w = 3
r = 1
while w <= 1001:
    j = w - 1
    for x in range(1,5):
        t = (j*x) + s
        r += t
    s = t
    w += 2

print r

