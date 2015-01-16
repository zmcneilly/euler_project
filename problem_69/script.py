#!env/bin/python

from math import sqrt
from math import ceil
from bitarray import bitarray

MAX = 1000000

def find_primes():
    primes = bitarray(MAX+1)
    primes.setall(True)

    for i in range(2, int(sqrt(MAX))+1, 1):
        if primes[i]:
            for j in range(i**2, MAX+1, i):
                primes[j] = False
    return primes

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def find_factors(n):
    result = set()
    if n < 0:
        n = n * -1
    m = int(sqrt(n))+1
    for i in range(2, m):
        if PRIMES[i]:
            if n % i == 0:
                result.add(i)
                n_i = int(n/i)
                if PRIMES[n_i]:
                    result.add(n_i)
    return result

def find_factors_tup(n):
    result = []
    if n < 0:
        n = n * -1
    for i in range(1, int(sqrt(n))+1, 1):
        if n % i == 0:
            result.append((i, int(n/i)))
    return result

@profile
def euler_totient(n, max_result=None):
    '''Return Euler's Totient of n'''
    factors = find_factors(n)
    results = set()
    for factor in factors:
        for m in range(factor, n, factor):
            results.add(m)
    return n - 1 - len(results)


@profile
def main():
    phi_n = {}
    max_phi = 4
    for n in range(2, MAX):
        if n not in phi_n:
            phi_n[n] = euler_totient(n)
            for p in range(2, max_phi):
                if p not in phi_n:
                    continue
                m = n*p
                if m > MAX:
                    break
                if n != p and gcd(p, n) == 1:
                    phi_n[m] = phi_n[n] * phi_n[p]
                    if m > max_phi:
                        max_phi = m
    max_n = 0
    max_phi = 0
    for n in phi_n:
        if n/phi_n[n] > max_phi:
            max_n = n
            max_phi = n/phi_n[n]

    print(max_n)

if __name__ == "__main__":
    global PRIMES
    PRIMES = find_primes()
    main()
