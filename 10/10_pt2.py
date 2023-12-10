# Taken solution from: https://pastebin.com/nikHkKZY

with open('10.txt', 'r') as file:
	my_input = file.read()

raw_data = my_input

lines = raw_data.split("\n")

def find_connections(x, y):
	found = []
	for direction in directions:
		if direction in connectors[lines[y][x]]:
			h, v = directions[direction]
			if 0 <= y + v < len(lines) and 0 <= h + x < len(lines[0]): 
				connector_found = lines[y + v][x + h]
				if backwards[direction] in connectors[connector_found]:
					found.append((x + h, y + v))
	return found
		
backwards = {
	'n'	:	's',
	's'	:	'n',
	'w'	:	'e',
	'e'	:	'w',
	}
	
connectors = {
	'|'	:	['n', 's'],
    '-'	:	['e', 'w'],
    'L'	:	['n', 'e'],
    'J'	:	['n', 'w'],
    '7'	:	['s', 'w'],
    'F'	:	['s', 'e'],
	'.'	:	[],
	'S'	:	['n', 's', 'w', 'e'],
	}
	
directions = {
	'n'	:	[0, -1],
	's'	:	[0, 1],
	'e'	:	[1, 0],
	'w'	:	[-1, 0],
	}

# make a second blank grid
distances = [['x'] * len(lines[0]) for x in range(len(lines))]

# find the starting point
for y, line in enumerate(lines):
	for x, symbol in enumerate(line):
		if symbol == 'S':
			distances[y][x] = 'S'
			next_points = [(x, y)]
			
while next_points:
	found = []
	for x, y in next_points:
		for newx, newy in find_connections(x, y):
			if distances[newy][newx] == 'x':
				# the second grid is still called distances from part 1 but
				# it's actually a clean map of the loop with no junk pipes.
				distances[newy][newx] = lines[newy][newx]
				found.append((newx, newy))
	next_points = found
	
# now to use the new clean grid to count points inside the loop
count = 0

for line in distances:
	inside = False
	pos = 0
	while pos < len(line):
		if line[pos] == 'x' and inside:
			count += 1
			pos += 1
		# if you cross a | you must go from out to in or vice versa
		elif line[pos] == '|':
			inside = not inside
			pos += 1
		elif line[pos] in ['-', 'x']:
			pos += 1
		else:
		# if you cross a corner piece then whether you end up inside
		# the loop depends on what type of other corner it's connected to
			block_start = line[pos]
			pos += 1
			while line[pos] == '-':
				pos += 1
			block_end = line[pos]
			if block_start + block_end in ['L7', 'FJ']:
				inside = not inside
			pos += 1
		
print(count)
# Ans is 423
				