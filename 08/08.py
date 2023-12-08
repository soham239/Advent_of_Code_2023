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

curr = 'AAA'
dist = 0
ind = 0
while curr != 'ZZZ':
    dist += 1
    c = first_line[ind % len(first_line)]
    if c == 'L':
        curr = adjacency_list[curr][0]
    else:
        curr = adjacency_list[curr][1]
    ind += 1

print(f"Total number of steps: {dist}")
