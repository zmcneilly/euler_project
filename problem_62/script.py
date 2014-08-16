#!env/bin/python
'''
Attempted Solution to Problem 62:

- Create a method to determine if a number is a cube.
- Create a loop to test if permutations of n**3 have exactly 5 cubes
- Return the smallest cube of the 5

Alternatively we can cube n and see when f(n**3) has the same digits as other
cubes. When a set of digits has 5 cubes associated to it, check all
permutations of those digits.
'''
from itertools import permutations
import math


def cube_root(n):
    "A modified Newton's Method solver for integral cube roots."
    if int(n) != n:
        raise ValueError("must provide an integer")
    if n in (-1,0,1): return True
    offset = (1,-1)[n > 0]
    x = n/2
    seen = set()
    steps = 0
    while 1:
        y = x**3
        if y == n:
            #~ print "Found %d ^ 1/3 = %d in %d steps" % (n,x,steps)
            return True
        dydx = 3.0*x*x
        x += int((n-y)/dydx)+offset
        x = x or 1
        if x in seen:
            return False
        seen.add(x)
        steps += 1


def number_to_list(n):
    '''
    Return n as a list of numbers
    '''
    __s = str(n)
    __l = [ int(c) for c in __s ]
    __l.sort()
    return __l


def list_to_number(l):
    '''
    Returns the integer generated from the list
    '''
    __s = list_to_string(l)
    return int(__s)


def list_to_string(l):
    __sl = [ str(c) for c in l ]
    return ''.join(__sl)

def p61_test(cube_list, last_cube):
    '''
    Takes as input a list of integers, and returns True if exactly 5
    permutations of that list are perfect cubes
    '''
    __min = last_cube**3
    for __l in permutations(cube_list):
        __n = list_to_number(__l)
        if __n < __min:
            continue
        elif cube_root(__n):
            return False
    return True

    test_list = [ list_to_number(__p) for __p in permutations(cube_list) ]
    test_set = set(test_list)
    first_cube = -1
    __n = last_cube
    __max = max(test_set)
    cube = __n**3
    while cube <= __max:
        if cube in test_set:
            return False
        __n += 1
        cube = __n**3
    return True

def main():
    '''
    The main function of the script
    '''
    results = {}
    first_cube = {}
    found = False
    __n = 345
    __max = {}
    result = ''
    while not found:
        cube = __n**3
        cube_list = number_to_list(cube)
        cube_string = list_to_string(cube_list)
        cube_number = int(cube_string)
        if cube_string not in results:
            results[cube_string] = 1
            first_cube[cube_string] = cube
        else:
            results[cube_string] += 1
        if results[cube_string] == 5:
            __max[cube_string] = int(cube_string[::-1])
            result = cube_list
        elif results[cube_string] > 5:
            __max[cube_string] = -1
            result = ''
        for max_string in __max:
            max_number = __max[max_string]
            if 0 < max_number < cube_number:
                result = max_string
                found = True
        __n += 1
    
    print result
    print first_cube[result]

if __name__ == '__main__':
    main()



