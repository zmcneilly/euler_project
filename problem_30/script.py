#!env/bin/python

r = []
t = 0
for x in range(2,200000):
    s = 0
    for c in str(x):
        s += int(c)**5
    if s == x:
        r.append(x)
        t += x
print r
print t

