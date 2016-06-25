#!/usr/bin/env python

from argparse import ArgumentParser
from datetime import datetime

# constants
FINISH_DAY = 66


def calculate(balance):
	"""
	Uses balance and the current day to figure out current daily budget
	"""
	# calculate the current day of year
	current_time = datetime.now()
	day = (current_time.month * 12) + current_time.day

	return balance / (FINISH_DAY - day)

def main():
	# pass relevant arguments with argparse
	parse = ArgumentParser(description="A tool for calculating how " + 
									   "much to spend in a day")
	parse.add_argument('money',type=int,default=0)
	args = parse.parse_args()

	# calculate budget and either print or return
	return calculate(args.money)


if __name__ == "__main__":
	print(main())