#!env/bin/python
#
# Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000
#

result = 0

for x in xrange(1,1001):

    result += x**x
    if result > 9999999999:
        result = result % 10**10

print result
