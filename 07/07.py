from collections import defaultdict

file_path = 'sample.txt'

# Store it as (what it is, sequence, bet)

# High card: A
# One pair: B
# Two pair: C
# Three of kind: D
# Full house: E
# Four of a kind: F
# Five of a kind: G

lines = []
with open(file_path, 'r') as file:
    
    for line in file:
        
        counts = defaultdict(int)
        
        for c in line.split()[0]:
            counts[c] += 1

        # Determine category
        if len(counts.keys()) == 1:
            # All 5 are same
            lines.append(('G', line.split()[0], int(line.split()[1])))
        elif len(counts.keys()) == 2:
            # could be 4+1 or 3+2
            for k,v in counts.items():
                if v == 1 or v == 4:
                    lines.append(('F', line.split()[0], int(line.split()[1])))
                    break
                if v == 2 or v == 3:
                    lines.append(('E', line.split()[0], int(line.split()[1])))
                    break
        elif len(counts.keys()) == 3:
            # 3+1+1, 2+2+1,
            for k,v in counts.items():
                if v == 3:
                    lines.append(('D', line.split()[0], int(line.split()[1])))
                    break
                if v == 2:
                    lines.append(('C', line.split()[0], int(line.split()[1])))
                    break
        elif len(counts.keys()) == 4:
            # only possible 2+1+1+1
            lines.append(('B', line.split()[0], int(line.split()[1])))
        else:
            # all are different
            lines.append(('A', line.split()[0], int(line.split()[1])))

# Replace chars so that natural sorting can help
mod_lines = []
for k, v, p in lines:
    v = v.replace('A', 'Z')
    v = v.replace('K', 'Y')
    v = v.replace('Q', 'X')
    v = v.replace('J', 'W')
    v = v.replace('T', 'V')
    v = v.replace('9', 'U')
    v = v.replace('8', 'T')
    v = v.replace('7', 'S')
    v = v.replace('6', 'R')
    v = v.replace('5', 'Q')
    v = v.replace('4', 'P')
    v = v.replace('3', 'O')
    v = v.replace('2', 'N')
    mod_lines.append((k,v, p))
    
mod_lines.sort()

total = 0
for i, v in enumerate(mod_lines):
    total += (i+1) * v[2]

print(f"Total is {total}")