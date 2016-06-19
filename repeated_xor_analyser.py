#!/usr/bin/env python

# Credit to to Gladius Maximus, whose solution
# I am partially copying for its use in other ctfs
# TODO: catch user input errors
# TODO: add argparse
# TODO: add support for plaintext with no spaces
# TODO: add support for printing key as ascii

import sys
from itertools import cycle, izip
from collections import Counter

def shift(text, k):
    return text[k:] + text[:k]

def count_same(a, b):
    c = 0
    for x, y in zip(a, b):
        if x == y:
            c += 1
    return c

def kasiski_examine(c, l=20):
    graph = ''
    for i in range(1, l):
        freq = count_same(c, shift(c, i))
        graph += '{0:< 3d} | {1:3d} |'.format(i, freq) + '=' * (freq / 4) + '\n'
    return graph

def multi_col_freq_analysis(ciphertext, key_len):
    frequencies = []
    for i in range(key_len):
        f = Counter()
        for ch in c[i::k_len]:
            f[ch] += 1
        frequencies.append(f)
    return frequencies

def xor(c, k):
    return ''.join(chr(x ^ y) for x, y in izip(c, cycle(k)))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} ciphertextfile keyfile'.format(sys.argv[0]))

    c = open(sys.argv[1], 'r').read()

    # Examine ciphertext using kasiski elimination
    m = input('Enter max keylength: ')
    print('Most likely key lengths:')
    print(kasiski_examine(c, m))
    print('')

    k_len = input('Please select a key length: ')

    # perform frequency analysis on each individual
    # column of text, where columns = key length
    f = multi_col_freq_analysis(c, k_len)

    k = []
    for freq in f:
        k_num = ord(' ') ^ ord(freq.most_common(1)[0][0])
        k.append(k_num)
    print(k)

    c_num = []
    for ch in c:
        c_num.append(ord(ch))

    print(xor(c_num, k))
    exit(0)
