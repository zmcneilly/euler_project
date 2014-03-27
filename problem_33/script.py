#!env/bin/python
err = 0
rn = 1
dn = 1

for n in range(10,100):
    ns = str(n)
    if ns[0] == ns[1]:
        continue
    for x in range(0,10):
        n0x = float(ns[0]+str(x))
        n1x = float(ns[1]+str(x))
        xn0 = float(str(n0x)[::-1])
        xn1 = float(str(n1x)[::-1])
        if ns[0] == str(x) or ns[1] == str(x):
            continue
        try:
            if n/n0x == float(ns[1])/x and ns[1] != str(x):
                rn *= n
                dn *= n0x
            if n/n1x == float(ns[0])/x and ns[0] != str(x):
                rn *= n
                dn *= n1x
            if n/xn0 == float(ns[1])/x and ns[1] != str(x):
                rn *= n
                dn *= xn0
            if n/xn1 == float(ns[0])/x and ns[0] != str(x):
                rn *= n
                dn *= xn1
        except ZeroDivisionError:
            err += 1 

print "{}/{}".format(str(rn),str(dn))
