#!/usr/bin/env python3
import sys

def capital_city(state):
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

    state_abbrev = states.get(state)
    if state_abbrev is None:
        print("Unknown state")
        return
    print(capital_cities[state_abbrev])

if __name__ == '__main__':
    if len(sys.argv) == 2:
        capital_city(sys.argv[1])
