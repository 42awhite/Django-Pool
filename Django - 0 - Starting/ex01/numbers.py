#!/usr/bin/env python3

def split_number():
    
    with open("numbers.txt", "r") as file:
        number = file.read()
    number = number.replace(',', '\n')
    print(number, end='')

if __name__ == '__main__':
	split_number()