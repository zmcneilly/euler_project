#!env/bin/python

import helpers, sys, math

top = 500

i = 1
lng = 1
while lng <= top:
    i += 1
    if i % 2 == 0:
        lng = len(helpers.find_factors(i/2)) * len(helpers.find_factors(i+1))
    else:
        lng = len(helpers.find_factors(i)) * len(helpers.find_factors((i+1)/2))
#    sys.stdout.write('\r')
#    sys.stdout.write('I:\t'+str(i)+'\tLen:\t'+str(lng))
#    sys.stdout.flush()

print '\n'
print str((i*(i+1))/2)
