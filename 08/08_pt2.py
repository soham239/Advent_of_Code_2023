import math

file_path = '08.txt'

# Open and read the file content
with open(file_path, 'r') as file:
    file_content = file.read()

# Split the file content into lines
lines = file_content.strip().split('\n')

# Get the first line in a list
first_line = lines[0]

# Create a graph node adjacency list
adjacency_list = {}

for line in lines[1:]:
    if line:
        # Split the line into node and its neighbors
        parts = line.split("=")
        node = parts[0].strip()
        neighbors_str = parts[1][2:-1]  # Remove parentheses
        neighbors = [neighbor.strip() for neighbor in neighbors_str.split(',')]

        # Add the node and its neighbors to the adjacency list
        adjacency_list[node] = neighbors

# Print the results
# print("First line in list:", first_line)
# print("Graph Node Adjacency List:", adjacency_list)

# get all starting points
starts = [k for k in adjacency_list.keys() if k[-1] == 'A']

def valid_end(curr):
    # print(curr)
    return sum([True for c in curr if c[-1] == 'Z']) == len(curr)

curr = starts
print(starts)

steps = []
for curr in starts:
    dist = 0
    ind = 0
    while curr[-1] != 'Z':
        dist += 1
        c = first_line[ind % len(first_line)]
        if c == 'L':
            curr = adjacency_list[curr][0]
        else:
            curr = adjacency_list[curr][1]
        ind += 1
    steps.append(dist)

print(steps)

def gcd(x, y):
    """Compute the greatest common divisor of x and y."""
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    """Compute the least common multiple of x and y."""
    return x * y // gcd(x, y)

def lcm_of_list(numbers):
    """Compute the least common multiple of a list of numbers."""
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result

# Example usage:
result = lcm_of_list(steps)
print(f"LCM is {result}")
