#!env/bin/python

import helpers as h
import sys

def get_int(n):
    s = ''
    for c in n:
        s += str(c)
    return int(s)

def get_str(n):
    s = ''
    for c in n:
        s += str(c)
    return s


for x in h.permute([9,8,7,6,5,4,3,2,1]):
    for i in range(1,9):
        for j in range(i+1,10):
            a,b,c = x[0:i],x[i:j],x[j:]
            ai=get_int(a)
            bi=get_int(b)
            if ai * 2 == bi and len(c) > 0:
                r = []
                ci = get_int(c)
                cs = get_str(c)
                rs = cs
                while len(rs) > 0:
                    for k in range(1,10):
                        p = rs.find(str(ai * k))
                        if p >= 0:
                            r.append(k)
                            rs = rs.replace(str(ai * k),'')
                            continue
                    break
                if len(rs) > 0:
                    continue
                else:
                    print x
                    print r
                    sys.exit(0)
            elif ai*2 == bi:
                print x
                sys.exit(0)
                    
