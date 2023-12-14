file_path = '14.txt'

# Open and read the file content
with open(file_path, 'r') as file:
    file_content = file.read()
    
# Split the file content into lines
lines = file_content.strip().split('\n')

supports = []
rock_counts = []
for i in range(len(lines[0])):
    support = []
    rocks = []
    rock_count = 0
    for j in range(len(lines)):
        if lines[j][i] == '#':
            support.append(j)
            rocks.append(rock_count)
            rock_count = 0
        elif lines[j][i] == 'O':
            rock_count += 1
    rocks.append(rock_count)
    support.append(len(lines))
    supports.append(support)
    rock_counts.append(rocks)

# print(rock_counts)
# print(supports)

total = 0
for i, rock in enumerate(rock_counts):
    # weight = len(lines)
    for j, c in enumerate(rock):
        weight = len(lines) - 1 - supports[i][j-1] if j >= 1 else len(lines)
        while c > 0:
            total += weight
            c -= 1
            weight -= 1
        

print(f"Ans is {total}")
# Ans is 105784
    