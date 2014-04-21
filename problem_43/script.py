#!env/bin/python

import helpers as h

def list_to_num(l):
    s = ''
    for e in l:
        s = s+str(e)
    return int(s)

def orig_test_prop(l):
    if list_to_num(l[1:4]) % 2 == 0 and\
        list_to_num(l[2:5]) % 3 == 0 and\
        list_to_num(l[3:6]) % 5 == 0 and\
        list_to_num(l[4:7]) % 7 == 0 and\
        list_to_num(l[5:8]) % 11 == 0 and\
        list_to_num(l[6:9]) % 13 == 0 and\
        list_to_num(l[7:10]) % 17 == 0:
        return True
    else:
        return False

def test_prop(l):
    if list_to_num(l[1:4]) % 2 == 0 and\
        list_to_num(l[2:5]) % 3 == 0 and\
        list_to_num(l[3:6]) % 5 == 0 and\
        list_to_num(l[4:7]) % 7 == 0 and\
        list_to_num(l[5:8]) % 11 == 0 and\
        list_to_num(l[6:9]) % 13 == 0:
#        list_to_num(l[6:9]) % 13 == 0 and\
#        list_to_num(l[7:10]) % 17 == 0:
        return True
    else:
        return False

t = 0

x = 6
n = 17*x
s17 = [n]
while n < 999:
    x += 1
    n = 17*x
    sn = str(n)
    if sn[0] != sn[1] and sn[0] != sn[2]:
        if sn[1] != sn[0] and sn[1] != sn[2]:
            if sn[2] != sn[1] and sn[2] != sn[0]:
                s17.append(n)
        

for s in s17:
    xp = [0,1,2,3,4,5,6,7,8,9]
    for c in str(s):
        xp.remove(int(c))
    for x in h.permute(xp):
        y = list(x)
        for c in str(s):
            y.append(int(c))
        if test_prop(y):
            t += list_to_num(y)
            print y

print t

