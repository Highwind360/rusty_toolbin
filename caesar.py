#!/usr/bin/env python3
"""
caesar.py
highwind

Given a caesar ciphertext string, display all the possible outcomes.
"""

import string
from sys import argv

ALPH = string.ascii_uppercase

def shift(mesg:str, key:int) -> str:
    return ''.join([ALPH[(ALPH.index(c) + key) % len(ALPH)] if c in ALPH else c for c in mesg])

def main():
    if len(argv) != 2:
        print("Usage: ./{} ciphertext")
        return

    ctxt = argv[1].upper()
    for k in range(1, 1 + len(ALPH)):
        print(shift(ctxt, k))


if __name__ == "__main__":
    main()
