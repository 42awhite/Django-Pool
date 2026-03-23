#!/usr/bin/env python3
from pathlib import Path


def parse_elements(filename):
	elements = []

	with open(filename, 'r', encoding='utf-8') as file:
		for raw_line in file:
			line = raw_line.strip()
			if not line:
				continue

			name, raw_data = line.split(' = ')
			fields = {}

			for part in raw_data.split(', '):
				key, value = part.split(':', 1)
				fields[key.strip()] = value.strip()

			electrons = fields['electron'].split()
			period = len(electrons)

			elements.append({
				'name': name,
				'position': int(fields['position']),
				'number': fields['number'],
				'symbol': fields['small'],
				'molar': fields['molar'],
				'electrons': fields['electron'],
				'period': period,
			})

	return elements


def build_grid(elements, rows=7, cols=18):
	grid = [[None for _ in range(cols)] for _ in range(rows)]

	for element in elements:
		row = element['period'] - 1
		col = element['position']
		if 0 <= row < rows and 0 <= col < cols:
			grid[row][col] = element

	return grid


def element_cell(element):
	return (
		'      <td style="border:1px solid #333; padding:10px; width:120px; '
		'height:120px; vertical-align:top;">\n'
		f'        <h4 style="margin:0 0 8px 0;">{element["name"]}</h4>\n'
		'        <ul style="margin:0; padding-left:18px;">\n'
		f'          <li>No {element["number"]}</li>\n'
		f'          <li>{element["symbol"]}</li>\n'
		f'          <li>{element["molar"]}</li>\n'
		f'          <li>{element["electrons"]} electron(s)</li>\n'
		'        </ul>\n'
		'      </td>\n'
	)


def empty_cell():
	return '      <td style="border:1px solid #333; width:120px; height:120px;"></td>\n'


def write_html(grid, filename):
	html = []
	html.append('<!DOCTYPE html>\n')
	html.append('<html lang="en">\n')
	html.append('<head>\n')
	html.append('  <meta charset="UTF-8">\n')
	html.append('  <title>Periodic Table</title>\n')
	html.append('</head>\n')
	html.append('<body>\n')
	html.append('  <table style="border-collapse:collapse;">\n')

	for row in grid:
		html.append('    <tr>\n')
		for cell in row:
			if cell is None:
				html.append(empty_cell())
			else:
				html.append(element_cell(cell))
		html.append('    </tr>\n')

	html.append('  </table>\n')
	html.append('</body>\n')
	html.append('</html>\n')

	with open(filename, 'w', encoding='utf-8') as file:
		file.writelines(html)


def main():
	base_dir = Path(__file__).resolve().parent
	input_file = base_dir / 'periodic_table.txt'
	output_file = base_dir / 'periodic_table.html'

	elements = parse_elements(input_file)
	grid = build_grid(elements)
	write_html(grid, output_file)
	print(f'Generated: {output_file}')


if __name__ == '__main__':
	main()
