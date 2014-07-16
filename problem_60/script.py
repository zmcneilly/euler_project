#!env/bin/python

import primes

prime_list = primes.PrimeNumbers()

def p60_test(to_check):
    for __x in to_check:
        for __y in to_check:
            if __x == __y:
                pass
            elif prime_list.is_prime(int(str(__x)+str(__y))) and \
                prime_list.is_prime(int(str(__y)+str(__x))):
                pass
            else:
                return False

    return True

def main():

    low_score = 1000000

    for x in xrange(3,10000000,2):
# Need to build the array of primes, this will be expensive
        if prime_list.is_prime(x) and x not in base:
            if p60_test(test_list):
                __s = sum(test_list)
                if __s < low_score:
                    print x
                    low_score = __s

    print low_score

if __name__ == '__main__':
    prime_list.load_prime_file()
    main()



