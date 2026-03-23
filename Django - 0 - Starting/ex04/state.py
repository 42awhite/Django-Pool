#!/usr/bin/env python3
import sys


def state(capital):
	states = {
		"Oregon": "OR",
		"Alabama": "AL",
		"New Jersey": "NJ",
		"Colorado": "CO"
	}

	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}

	for state_name, abbreviation in states.items():
		if capital_cities[abbreviation] == capital:
			print(state_name)
			return

	print("Unknown capital city")


if __name__ == '__main__':
	if len(sys.argv) == 2:
		state(sys.argv[1])
