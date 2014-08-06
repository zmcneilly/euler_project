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
    _max = 10000

    for a in xrange(3,_max,2):
        if not prime_list.is_prime(a):
            continue
        for b in xrange(a+2,_max,2):
            if not prime_list.is_prime(b):
                continue
            for c in xrange(b+2,_max,2):
                if not prime_list.is_prime(c):
                    continue
                for d in xrange(c+2,_max,2):
                    if prime_list.is_prime(d):
                        test_list = [a,b,c,d]
                        if p60_test(test_list):
                            __s = sum(test_list)
                            if __s < low_score:
                                print test_list
                                low_score = __s

    print low_score

if __name__ == '__main__':
    prime_list.load_prime_file()
    main()



