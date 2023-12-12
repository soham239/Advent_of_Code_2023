from collections import deque
from math import comb

file_path = '11.txt'

# Open and read the file content
with open(file_path, 'r') as file:
    file_content = file.read()
    
# Split the file content into lines
lines = file_content.strip().split('\n')

# Get the rows and cols that need expansion
rows = set(range(len(lines)))
cols = set(range(len(lines[0])))

ROWS, COLS = len(lines), len(lines[0])
sources = []
for r in range(ROWS):
    for c in range(COLS):
        if lines[r][c] == '#':
            # Remove from both sets as there is a galaxy here
            sources.append((r,c))
            if r in rows:
                rows.remove(r)
            if c in cols:
                cols.remove(c)

rows = list(rows)
cols = list(cols)
rows.sort()
cols.sort()
# now rows and cols have only the expansion ones

total = 0
for i in range(len(sources)):
    for j in range(i+1, len(sources)):
        x, y = sources[i]
        a, b = sources[j]
        
        if x > a:
            x, a = a, x
        if y > b:
            y, b = b, y
        dist = b - y + a - x
        # account for expansion
        for r in rows:
            if x < r < a:
                dist += 999999
                # Modify only dist values for part 2
        
        for c in cols:
            if y < c < b:
                dist += 999999
                # Modify only dist values for part 2
        
        total += dist

print(f"Total is {total}")
# For part 1: Total is 10165598
# For part 2: Total is 678728808158
    