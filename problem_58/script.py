#!env/bin/python
import primes as p

primes = p.PrimeNumbers()
primes.load_prime_file()

def odd_num(n):
    """
    This functions returns the nth odd number
    """
    return n*2 - 1

def diag(n,pos):
    """
    This function returns the nth number of the series of numbers on the diag
    indicated by the pos variable.

    pos = 0 : This is the diagonal to the bottom right
    pos = 1 : This is the diagonal to the bottom left
    pos = 2 : This is the diagonal to the top left
    pos = 3 : This is the diagonal to the top right
    """
    num = odd_num(n)
    return num**2-((num-1)*pos)

def percent_prime(nums):
    """
    This function returns the percent of the list of numbers that is prime
    """
    global primes

    _p = 0.0
    for num in nums:
        if primes.is_prime(num):
            _p += 1
    return _p

def main():
    """
    This function is the main function
    """
    global primes
    noOfPrimes = 3
    sl = 2
    c = 9
    test = float(noOfPrimes)/(2*sl+1)
    while test >= 0.10:
        sl += 2
        for i in xrange(0,3):
            c += sl
            if primes.is_prime(c):
                noOfPrimes += 1
        c += sl
        test = float(noOfPrimes)/(2*sl+1)
    print sl + 1

if __name__ == '__main__':
    main()
