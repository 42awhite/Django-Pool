#!/usr/bin/env python3

def print_dictionary(music_dic):
    for key, value in music_dic.items():
        print(f"{key}: {value}")

def musician_dictionary():
    d = [
		('Hendrix' , '1942'),
		('Allman' , '1946'),
		('King' , '1925'),
		('Clapton' , '1945'),
		('Johnson' , '1911'),
		('Berry' , '1926'),
		('Vaughan' , '1954'),
		('Cooder' , '1947'),
		('Page' , '1944'),
		('Richards' , '1943'),
		('Hammett' , '1962'),
		('Cobain' , '1967'),
		('Garcia' , '1942'),
		('Beck' , '1944'),
		('Santana' , '1947'),
		('Ramone' , '1948'),
		('White' , '1975'),
		('Frusciante', '1970'),
		('Thompson' , '1949'),
		('Burton' , '1939')
	]
    music_dic = {}
    for name, year in d:
        music_dic[year] = name
    print_dictionary(music_dic)

if __name__ == '__main__':
    musician_dictionary()

