#!env/bin/python

#It can be seen that the number, 125874, and its double, 251748, contain exactly
#the same digits, but in a different order.
#
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
#contain the same digits.
#

def same_chars(n1,n2):
    ln1 = list(str(n1))
    ln2 = list(str(n2))
    
    ln1.sort()
    ln2.sort()

    return ln1 == ln2


done = False
n = 1

while not done:
    for x in xrange(2,7):
        if same_chars(n,x*n):
            done = True
        else:
            done = False
            break
    n += 1

print n -1
