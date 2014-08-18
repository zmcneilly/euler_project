#!env/bin/python
'''
This script will return the number of numbers with n digits which are also
n-power integers.

Starting with n = 1 and m = 1 we will compute m^n = r until len(r) > n
We will increment n until len(9^n) != n
'''

def main():
    '''
    This is the main method of the script
    '''
    __n = 1
    count = 0
    while len(str(9**__n)) == __n:
        __m = 1
        r = __m**__n
        while len(str(r)) <= __n:
            if len(str(r)) == __n:
                print "{}^{} = {}".format(__m, __n, r)
                count += 1
            __m += 1
            r = __m**__n
        __n += 1
    print count

if __name__ == "__main__":
    main()


