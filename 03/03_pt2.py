from collections import defaultdict

file_path = '03.txt'  

total = 0

with open(file_path, 'r') as file:
    lines = []
    for line in file:
        lines.append(line.strip())

m = len(lines)
n = len(lines[0])
    
star_map = defaultdict(list)

def is_valid(num, r, c):
    # num ends at r,c
        # check previous line
        for i in range(c-len(str(num))-1, c+1):
            if is_valid_pos(r-1, i):
                star_map[(r-1, i)].append(num)
       
        # check current line
        if is_valid_pos(r, c-len(str(num))-1):
            star_map[(r, c-len(str(num))-1)].append(num)
        if is_valid_pos(r, c):
            star_map[(r, c)].append(num)
        
        # check next line
        for i in range(c-len(str(num))-1, c+1):
            if is_valid_pos(r+1, i):
                star_map[(r+1, i)].append(num)
    
def is_valid_pos(r, c):
    if r < 0 or r >= m or c < 0 or c >= n or lines[r][c] != '*':
        return False
    return True
    
for r, line in enumerate(lines):
    num = []
    for i, c in enumerate(line):
        if c.isdigit():
            num.append(c)
        else:
            if num:
                num = int(''.join(num))
                is_valid(num, r, i)
                num = []
    # number could be end of line
    if num:
        i += 1
        num = int(''.join(num))
        is_valid(num, r, i)
        num = []

gears = [v[0]*v[1] for k,v in star_map.items() if len(v) == 2]
print(f"Total is {sum(gears)}")
    