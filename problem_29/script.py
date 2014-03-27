#!env/bin/python

l = []

for a in range(2,101):
    for b in range(2,101):
        l.append(a**b)

s = set(l)
print len(s)

