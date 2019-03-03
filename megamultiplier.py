#!/usr/bin/env python3
"""
megamultiplier.py
highwind

Prints the product of all divisors of a given N
"""
from sys import argv
from functools import reduce
from itertools import combinations

# Like sum, but multiplication
mult = lambda things: reduce(lambda x,y: x*y, things)
# Turns a 3D array into a 1D array
smash = lambda l: [item for sublist in l for two_d_list in sublist for item in two_d_list]

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
    print(mult(smash([combinations(factors, i) for i in range(1, len(factors)+1)])))

if __name__ == "__main__":
    main()
