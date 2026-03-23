#!/usr/bin/env python3

def split_number(fd):
    for number in fd:
        number = number.split(',')
        print(number)

if __name__ == '__main__':
	with open('numbers.txt', 'r') as fd:
		split_number(fd)