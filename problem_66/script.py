#!env/bin/python
'''This script will solve Problem 66 on Project Euler.
For an explanation of the algorithm used to solve this, visit:
http://mathworld.wolfram.com/PellEquation.html'''
from math import sqrt, ceil, floor
import helpers as h
MAX = 1000


def is_square(number):
    '''This function returns True if a number is a natural square and false
    otherwise.'''
    square_rt = sqrt(number)
    return ceil(square_rt) == square_rt


def main():
    '''The main function of this script.'''
    # First we generate the set of numbers we want to test
    D_set = [__x for __x in range(0, MAX+1) if not is_square(__x)]
    max_x = 0
    max_D = 0
    for D in D_set:
        # a should be the full fraction expansion
        a0, a_remain = h.continued_fraction_expansion(D)
        a = [a0]
        a.extend(a_remain)
        # p and q will need to be at least as long as 2r+1
        r = a.index(2*a[0])-1
        while (2*r+1) > len(a):
            a.extend(a[1:])
        # This is the algorithm found at:
        # http://mathworld.wolfram.com/PellEquation.html
        p = [a[0], (a[0] * a[1] + 1)]
        q = [1, a[1]]
        P = [0, a[0]]
        Q = [1, (D - a[0]**2)]
        for n in range(2, len(a)):
            p.append(a[n]*p[n-1]+p[n-2])
            q.append(a[n]*q[n-1]+q[n-2])
            P.append(a[n-1]*Q[n-1]-P[n-1])
            Q.append((D-P[n]**2)/(Q[n-1]))
        if r > 0 and r % 2 > 0:
            x = p[r]
        else:
            x = p[2*r+1]
        if x > max_x:
            max_x = x
            max_D = D
    print(max_D)


if __name__ == "__main__":
    main()
