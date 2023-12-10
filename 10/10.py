from collections import defaultdict, deque

# transform input
file_path = '10.txt'

# Open and read the file content
with open(file_path, 'r') as file:
    file_content = file.read()
    
# Split the file content into lines
lines = file_content.strip().split('\n')

possible_path = defaultdict(list)
# for a position I store entry and exit points as tuples

# in first iteration pre-process input and also note the starting point
ROWS, COLS = len(lines), len(lines[0])

def is_valid(r, c):
   return r >= 0 and c >= 0 and r < ROWS and c < COLS

start_r = start_c = 0
for r in range(ROWS):
    for c in range(COLS):
        if lines[r][c] == 'S':
            start_r, start_c = r, c
        elif lines[r][c] == '|':
            if is_valid(r-1, c) and is_valid(r+1, c):
                possible_path[(r,c)].append(((r-1, c)))
                possible_path[(r,c)].append(((r+1, c)))
            else:
                # only note the point exists - no valid path
                possible_path[(r,c)].append('.')
        elif lines[r][c] == '-':
            if is_valid(r, c-1) and is_valid(r, c+1):
                possible_path[(r,c)].append(((r, c-1)))
                possible_path[(r,c)].append(((r, c+1)))
            else:
                # only note the point exists - no valid path
                possible_path[(r,c)].append('.')
        elif lines[r][c] == 'L':
            if is_valid(r-1, c) and is_valid(r, c+1):
                possible_path[(r,c)].append(((r-1, c)))
                possible_path[(r,c)].append(((r, c+1)))
            else:
                # only note the point exists - no valid path
                possible_path[(r,c)].append('.')
        elif lines[r][c] == 'J':
            if is_valid(r-1, c) and is_valid(r, c-1):
                possible_path[(r,c)].append(((r-1, c)))
                possible_path[(r,c)].append(((r, c-1)))
            else:
                # only note the point exists - no valid path
                possible_path[(r,c)].append('.')
        elif lines[r][c] == '7':
            if is_valid(r+1, c) and is_valid(r, c-1):
                possible_path[(r,c)].append((r+1, c))
                possible_path[(r,c)].append((r, c-1))
            else:
                # only note the point exists - no valid path
                possible_path[(r,c)].append('.')
        elif lines[r][c] == 'F':
            if is_valid(r+1, c) and is_valid(r, c+1):
                possible_path[(r,c)].append(((r+1, c)))
                possible_path[(r,c)].append(((r, c+1)))
            else:
                # only note the point exists - no valid path
                possible_path[(r,c)].append('.')

        
# Now we run BFS and store dist in tuple 
# till we run out of input that gives max length

# Starting point in queue
queue = deque([(start_r,start_c,0)])
visited = set()
max_dist = 0
# print(possible_path)
while queue:
    r, c, dist = queue.popleft()
    max_dist = max(dist, max_dist)
    visited.add((r, c))
    dist += 1
    for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
        new_r = r + dx
        new_c = c + dy
        if is_valid(new_r, new_c) and (new_r, new_c) not in visited:
            # check if I am a valid entry point
            # print(f"{new_r=} {new_c=} ")
            if (r, c) in possible_path[(new_r,new_c)]:
                queue.append((new_r, new_c, dist))

print(f"Ans is {max_dist}")
# Ans is 6697