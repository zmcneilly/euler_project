#!env/bin/python
'''This script will solve Problem 66 on Project Euler.'''
from math import sqrt, ceil
MAX = 1000


def is_square(number):
    '''This function returns True if a number is a natural square and false
    otherwise.'''
    square_rt = sqrt(number)
    return ceil(square_rt) == square_rt


def d_larger_than(min_y, max_y, D_set):
    '''Return a list, containing all values of D that do not have a solution
    for x below a maximum'''
    result = []
    for D in D_set:
        if is_square(D):
            continue
        y = min_y
        x = sqrt(1 + D*y*y)
        while ceil(x) != x:
            if y >= max_y:
                result.append(D)
                break
            y += 1
            x = sqrt(1 + D*y*y)
    return result


def main():
    '''The main function of this script.'''
    D_set = [__x for __x in range(0, MAX+1)]
    y = 5
    D_set = d_larger_than(1, y, D_set)
    length = len(D_set)
    while length > 1:
        min_y = y
        y += len(D_set)
        D_set = d_larger_than(min_y, y, D_set)
        __l = len(D_set)
        if __l != length:
            length = __l
            print(length)
    print(D_set)



if __name__ == "__main__":
    main()
