#!/usr/bin/env python3
"""
megamultiplier.py
highwind

Factorizes an integer argument
"""
from sys import argv
from functools import reduce
from itertools import combinations

# Like sum, but multiplication
mult = lambda things: reduce(lambda x,y: x*y, things)
# Turns a 2D array into a 1D array
flatten = lambda l: [item for sublist in l for item in sublist]

# Credit: https://stackoverflow.com/a/16996439
def factorize_primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def main():
    if len(argv) != 2:
        print("Usage: %s int" % argv[0])
        return

    factors = factorize_primes(int(argv[1]))
    # multiplies every possible combination of 'factors' together
    print(mult(map(mult, flatten([combinations(factors, i) for i in range(1, len(factors)+1)]))))

if __name__ == "__main__":
    main()
