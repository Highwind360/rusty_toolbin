#!/usr/bin/env python3
"""
A tool for encrypting and decrypting substitution ciphers.

Currently only ecrypts.
TODO: write a decrypt method
"""

from string import ascii_uppercase, ascii_lowercase
from argparse import ArgumentParser


def encrypt(plaintext, key):
    """Encrypts a plaintext using the key.

    key - the key to use: a series of 26 unique alphabetic characters.
    plaintext - the plaintext to encrypt. Will only encipher alphabetic
    characters, ignoring the rest.

    This returns the ciphertext as a string.
    """

    keyup = key.upper()
    ciphertext = ''
    if len(keyup) != 26 or not all_chars_are_unique_and_alphabetic(keyup):
        raise TypeError("Key must be 26 unique alphabetic characters.")

    for c in plaintext.upper():
        if ascii_uppercase.__contains__(c):
            index_of_char = ascii_uppercase.index(c)
            ciphertext += keyup[index_of_char]
        else:
            ciphertext += c

    return ciphertext

def all_chars_are_unique_and_alphabetic(thing):
    """Checks that parameter has only unique, alphabetic characters."""
    alphabet = ascii_lowercase + ascii_uppercase

    # Gets a list of all the unique elements of thing
    thing2 = list(set(thing))
    is_unique = len(thing) == len(thing2)

    is_alphabetic = True
    for element in thing:
        is_alphabetic = is_alphabetic and alphabet.__contains__(element)

    return is_alphabetic and is_unique

def main():
    """Encrypts/decrypts using monoalphabetic substitution ciphers.
    When called, this program will require a key and some ciphertext, and will
    use the key to create some ciphertext. It is possible to specify an input
    file and/or an output file, but a key is necessary.

    TODO: implement a decryption option
    """
    parser = ArgumentParser(description="Encrypts/decrypts using " +
                            "monoalphabetic substitution ciphers.")
    parser.add_argument('key', help='key to encrypt/decrypt with')
    parser.add_argument('-f', '--infile', default=None, required=False,
                        help='input file for plaintext')
    parser.add_argument('-o', '--outfile', default=None, required=False,
                        help='output file for ciphertext')
    args = parser.parse_args()

    if args.infile == None:
        ptxt = input("Hi! What's the text you'd like to encrypt? ")
    else:
        ptxt = open(args.infile, 'r').read()

    ctxt = encrypt(ptxt, args.key)
    if args.outfile == None:
        print(ctxt)
    else:
        open(args.outfile, 'w').write(ctxt)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + "Oh...okay...Goodbye!")
