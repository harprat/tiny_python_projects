#!/usr/bin/env python3

import argparse
"""
Author: Haris
Purpose: Say hello
"""

def get_args():
	"""Get the command line argument"""

	parser = argparse.ArgumentParser(description='Say hello!')
	parser.add_argument('-n', '--name', metavar='name',
						default='World', help='Name to greet')
	return parser.parse_args()

def main():
	"""Print Hello with argument"""

	args = get_args()
	print('Hello, ' + args.name + '!')

if __name__ == '__main__':
	main()
