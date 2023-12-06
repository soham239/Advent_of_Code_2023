file_path = '06.txt'  

lines = []
with open(file_path, 'r') as file:
    
    for line in file:
        lines.append(line)

time_values = list(map(int, lines[0].split()[1:]))

# Extract values for Distance
distance_values = list(map(int, lines[1].split()[1:]))

time = int(''.join([str(t) for t in time_values]))
dist = int(''.join([str(t) for t in distance_values]))

# Print the results
print("Time values:", time)
print("Distance values:", dist)

for j in range(time):
    if j * (time-j) > dist:
        # found the threshold
        ways = time-j-j+1
        break

print(ways)