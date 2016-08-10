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


# TODO: move password generation to its own function
def main(pwd_length=12):
	password, charset = '', ''
	if True: # TODO: add conditions to add only desired chars to charset
		charset += printable[:-38]
	
	for i in range(pwd_length):
		pick_index = randrange(len(charset))
		password += charset[pick_index]
	
	print(password)


if __name__ == "__main__":
	if len(argv) > 2:
		print("Usage: {name} pwd_length".format(name = argv[0]))
	elif len(argv) == 2:
		main(int(argv[1]))
	else:
		main()
