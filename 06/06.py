file_path = '06.txt'  

lines = []
with open(file_path, 'r') as file:
    
    for line in file:
        lines.append(line)

time_values = list(map(int, lines[0].split()[1:]))

# Extract values for Distance
distance_values = list(map(int, lines[1].split()[1:]))

# Print the results
print("Time values:", time_values)
print("Distance values:", distance_values)
prod = 1
for i in range(len(time_values)):
    time = time_values[i]
    dist = distance_values[i]
    
    for j in range(time):
        if j * (time-j) > dist:
            # found the threshold
            ways = time-j-j+1
            prod = prod * ways
            break

print(prod)