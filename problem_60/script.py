#!env/bin/python

import primes

prime_list = primes.PrimeNumbers()

def p60_test(to_check):
    __x = to_check[len(to_check)-1]
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

    plist = []

    for __x in xrange(3,_max,2):
        if prime_list.is_prime(__x):
            plist.append(__x)

    for a in plist:
        for b in plist:
            if b <= a or not p60_test([a,b]):
                continue
            for c in plist:
                if c <= b or not p60_test([a,b,c]):
                    continue
                for d in plist:
                    if d <= c or not p60_test([a,b,c,d]):
                        continue
                    for e in plist:
                        if e <= d:
                            continue
                        test_list = [a,b,c,d,e]
                        if p60_test(test_list):
                            __s = sum(test_list)
                            if __s < low_score:
                                print test_list
                                low_score = __s
                                print low_score
                                return 0


if __name__ == '__main__':
    prime_list.load_prime_file()
    main()



