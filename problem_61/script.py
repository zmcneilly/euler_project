#!env/bin/python

from itertools import permutations

def triangle_nums(max_num):
    '''
    Returns a list of triangle numbers from n = 1 .. max_num
    n*(n+1)/2
    '''
    result = []

    for n in xrange(1,max_num+1):
        __r = (n*(n+1)/2)
        if 999 < __r < 9999:
            result.append(__r)

    return result

def square_nums(max_num):
    '''
    Return a list of square numbders from n = 1 .. max_num
    n**2
    '''
    result = []

    for n in xrange(1,max_num+1):
        __r = (n**2)
        if 999 < __r < 9999:
            result.append(__r)

    return result

def pentagonal_nums(max_num):
    '''
    Return a list of pentagonal numbders from n = 1 .. max_num
    n*(3*n-1)/2
    '''
    result = []

    for n in xrange(1,max_num+1):
        __r = (n*(3*n-1)/2)
        if 999 < __r < 9999:
            result.append(__r)

    return result

def hexagonal_nums(max_num):
    '''
    Return a list of hexagonal numbders from n = 1 .. max_num
    n*(2*n-1)
    '''
    result = []

    for n in xrange(1,max_num+1):
        __r = (n*(2*n-1))
        if 999 < __r < 9999:
            result.append(__r)

    return result

def heptagonal_nums(max_num):
    '''
    Return a list of heptagonal numbders from n = 1 .. max_num
    n*(5*n-3)/2
    '''
    result = []

    for n in xrange(1,max_num+1):
        __r = (n*(5*n-3)/2)
        if 999 < __r < 9999:
            result.append(__r)

    return result

def octagonal_nums(max_num):
    '''
    Return a list of ocatgonal numbders from n = 1 .. max_num
    n*(3*n-2)
    '''
    result = []

    for n in xrange(1,max_num+1):
        __r = (n*(3*n-2))
        if 999 < __r < 9999:
            result.append(__r)

    return result

def cyclic(test_list):
    '''
    This function takes as an input a list of numbers and returns true if they
    can be arranged cyclically
    '''
    for __l in permute(test_list):
        result = True
        if str(__l[0])[0:2] != str(__l[len(__l)-1])[2:4]:
            continue
        for x in xrange(1,len(__l)-1):
            if str(__l[x-1])[2:4] == str(__l[x])[0:2] and \
                str(__l[x])[2:4] == str(__l[x+1])[0:2]:
                pass
            else:
                result = False
                break
        if result:
            return result
    return False

def cyclic_ordered(test_list):
    '''
    This function takes as an input a list of numbers, sorts them, and returns
    true if they can be arranged cyclically
    '''
    test_list.sort()
    __l = test_list
    result = True
    if str(__l[0])[0:2] != str(__l[len(__l)-1])[2:4]:
        return False

    for x in xrange(1,len(__l)-1):
        if str(__l[x-1])[2:4] == str(__l[x])[0:2] and \
            str(__l[x])[2:4] == str(__l[x+1])[0:2]:
            pass
        else:
            return False

    return test_list

def count_instances(a, b):
    '''
    This will return the number of common elements between a and b
    '''
    _la = len(a)
    _lb = len(b)
    if _lb > _la:
        large = set(b)
        small = a
    else:
        large = set(a)
        small = b

    count = 0

    for x in small:
        if x in large:
            count += 1

    return count

def first_instance(a, b):
    '''
    This will return the first common element between a and b
    '''
    _la = len(a)
    _lb = len(b)
    if _lb > _la:
        large = set(b)
        small = a
    else:
        large = set(a)
        small = b

    for x in small:
        if x in large:
            return x

    return None

def tuple_to_string(t):
    '''
    This takes a tuple as input and returns that tuple as a string
    '''
    result = ''
    for x in t:
        result += str(x)
    return result

def main():
    '''
    The main method of this script
    '''
    __s = [ x for x in xrange(0,10) ] 
    _max = 10000
    # We generate the set of possible triagle, square, pentagonal, hexagonal,
    # heptagonal, and octagonal numbers.
    tri_nums = triangle_nums(_max)
    squ_nums = square_nums(_max)
    pen_nums = pentagonal_nums(_max)
    hex_nums = hexagonal_nums(_max)
    hep_nums = heptagonal_nums(_max)
    oct_nums = octagonal_nums(_max)
    # A list of all possible numbers
    all_nums = tri_nums + squ_nums + pen_nums + hex_nums + hep_nums + oct_nums
    # Instead of generating a set and checking if it is cyclic, we will
    # generate only cyclic sets. The first number can be any 4 digit number. We
    # generate this with itertools' permutations method.
    for _p1 in permutations(__s,4):
        _s1 = tuple_to_string(_p1)
        _i1 = int(_s1)
        # If the number generated is not in our list of numbers we need a new
        # number.
        if _i1 not in all_nums:
            continue
        # The 2nd, 3rd, 4th, and 5th numbers take the first two digits and then
        # permute through all possible combinations for the last two digits. We
        # only use numbers which are in one of the sets.
        for _p2 in permutations(__s,2):
            _s2 = _s1[2:4] + tuple_to_string(_p2)
            _i2 = int(_s2)
            if _i2 not in all_nums:
                continue
            for _p3 in permutations(__s,2):
                _s3 = _s2[2:4] + tuple_to_string(_p3)
                _i3 = int(_s3)
                if _i3 not in all_nums:
                    continue
                for _p4 in permutations(__s,2):
                    _s4 = _s3[2:4] + tuple_to_string(_p4)
                    _i4 = int(_s4)
                    if _i4 not in all_nums:
                        continue
                    for _p5 in permutations(__s,2):
                        _s5 = _s4[2:4] + tuple_to_string(_p5)
                        _i5 = int(_s5)
                        if _i5 not in all_nums:
                            continue
                        # The 6th number is composed of the last two digits of
                        # the 5th number and the first two digits of the 1st
                        # number.
                        _s6 = _s5[2:4] + _s1[0:2]
                        _i6 = int(_s6)
                        if _i6 not in all_nums:
                            continue
                        t_set = [_i1,_i2,_i3,_i4,_i5,_i6]
                        result = list(t_set)
                        # We now need to test for the condition of each type of
                        # number being represented once. We check our full set
                        # against the sets by order of how many numbers are in
                        # that set. A particular number is least likely to be
                        # an oct number, hep, hex, etc.
                        try:
                            t_set.remove(first_instance(t_set,oct_nums))
                            t_set.remove(first_instance(t_set,hep_nums))
                            t_set.remove(first_instance(t_set,hex_nums))
                            t_set.remove(first_instance(t_set,pen_nums))
                            t_set.remove(first_instance(t_set,squ_nums))
                            t_set.remove(first_instance(t_set,tri_nums))
                        except ValueError:
                            continue
                        if len(t_set) < 1:
                            print "Set:"
                            print result
                            print "Sum:"
                            print sum(result)
                            return 0

if __name__ == "__main__":
    main()
