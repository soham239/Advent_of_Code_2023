def horizontal(lines):
    n = len(lines)
    for i in range(n-1):
        if lines[i] == lines[i+1]:
            # possible start point
            s, e = i, i+1
            while s >= 0 and e < n:  
                if lines[s] != lines[e]:
                    break
                s -= 1
                e += 1
            else:
                # never went to break so found solution
                return 100 * (i+1)  
    return -1
            
def vertical(lines):
    # rotate input
    lines = list(zip(*lines))
    n = len(lines)
    for i in range(n-1):
        if lines[i] == lines[i+1]:
            # possible start point
            s, e = i, i+1
            while s >= 0 and e < n:  
                if lines[s] != lines[e]:
                    break
                s -= 1
                e += 1
            else:
                # never went to break so found solution
                return i+1
    return -1           

file_path = "13.txt"

total = 0
with open(file_path, 'r') as file:
    while True:
        # Read lines until the next empty line
        current_lines = []
        line = file.readline().strip()
        while line:
            current_lines.append(line)
            line = file.readline().strip()

        # Print or process the current set of lines
        if current_lines:
            
            num = horizontal(current_lines)
            if num == -1:
                num = vertical(current_lines)
        
            total += num
        else:
            break

print(f"Ans is {total}")