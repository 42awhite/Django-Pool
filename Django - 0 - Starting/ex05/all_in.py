#!/usr/bin/env python3
import sys

def normalize_text(text):
	return " ".join(text.strip().lower().split())

def all_in(expressions):
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

	# If two commas are successive, the script prints nothing.
	if ",," in expressions:
		return

	tokens = expressions.split(',')

	normalized_states = {}
	for state_name in states:
		normalized_states[normalize_text(state_name)] = state_name

	normalized_capitals = {}
	for abbreviation, capital_name in capital_cities.items():
		normalized_capitals[normalize_text(capital_name)] = abbreviation

	for token in tokens:
		expression = token.strip()

		# Empty expressions (e.g. ", ,") are ignored.
		if expression == "":
			continue

		normalized_word = normalize_text(expression)

		if normalized_word in normalized_states:
			state_name = normalized_states[normalized_word]
			abbreviation = states[state_name]
			capital_name = capital_cities[abbreviation]
			print(f"{capital_name} is the capital of {state_name}")
			continue

		if normalized_word in normalized_capitals:
			abbreviation = normalized_capitals[normalized_word]
			capital_name = capital_cities[abbreviation]
			matching_state = ""

			for state_name, state_abbreviation in states.items():
				if state_abbreviation == abbreviation:
					matching_state = state_name
					break

			print(f"{capital_name} is the capital of {matching_state}")
			continue

		print(f"{expression} is neither a capital city nor a state")


if __name__ == '__main__':
	if len(sys.argv) == 2:
		all_in(sys.argv[1])
