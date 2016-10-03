#!/usr/bin/env python3

"""
    password_tool.py
    Grayson Sinclair

    Generates a random password for the user.
    TODO: Use argparse for arguments
    TODO: generate random password
    TODO: add options...
        ...for password details:
            - include punctuation
            - only lowercase
            - only uppercase
            - no numbers
        ...output password to file
        ...take username for replacing default username in file
        ...batch usernames/passwords
    TODO: use sqlite to create database for password management
        - Make database encrypted w/password management
"""

from sys import argv
from string import printable
from random import randrange


def password_generator(charset, length):
    """The password generation function.

    This takes a set of characters and
    composes a random password out of them.
    """
    password = ''

    for i in range(length):
        pick_index = randrange(len(charset))
        password += charset[pick_index]

    return password

def compose_charset(options):
    """Chooses a set of characters to generate a password with.

    The user can specifify a series of options for sets of characters to add to
    the overall character set. If nothing is specified, a default set of
    characters are included, instead.
    """
    charset = ''

    if False: # TODO: add conditions to add only desired chars to charset
        pass
    else:
        # the default set of characters
        charset += printable[:-38]

    return charset

def main(pwd_length=12, charset_options=[]):
    """The main function.

    pwd_length - the length of the password to generate as an int.
    charset_options - a list of character sets to add to the master charset.
    """
    charset = compose_charset(charset_options)
    print(password_generator(charset, pwd_length))


if __name__ == "__main__":
    # TODO: handle arguments with argparse
    if len(argv) > 2:
        print("Usage: {name} pwd_length".format(name = argv[0]))
    elif len(argv) == 2:
        main(int(argv[1]))
    else:
        main()
