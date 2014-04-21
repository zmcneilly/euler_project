#!env/bin/python

import helpers as h

pMAX = 0
MAX = 100
pnums = []
done = False

while not done:
    for x in xrange(pMAX+1,MAX+1):
        pnums.append(h.pentagonal_num(x))
    pset = set(pnums)

    for x in xrange(0,MAX):
        px = pnums[x]
        for y in xrange(max(pMAX,x),MAX):
            py = pnums[y]
            if (py - px) in pset:
                if h.test_pentagonal_num(py+px):
                    print 'Difference of P({}) and P({}) = {}'.format(x+1,y+1,py-px)
                    print 'Sum of P({}) and P({}) = {}'.format(x+1,y+1,py+px)
                    print 'D = {}'.format(abs(px-py))
                    done = True
                    MAX = 0
                    break
                if x+1 == 1020 and y+1 == 2167:
                    print "Why does this miss?"
    pMAX,MAX = MAX,2*MAX

