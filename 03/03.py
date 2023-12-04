file_path = '03.txt'  

total = 0

with open(file_path, 'r') as file:
    lines = []
    for line in file:
        lines.append(line.strip())

m = len(lines)
n = len(lines[0])
    
def is_valid(num, r, c):
    # num ends at r,c
        # check previous line
        for i in range(c-len(str(num))-1, c+1):
            if is_valid_pos(r-1, i):
                return True
       
        # check current line
        if is_valid_pos(r, c-len(str(num))-1) or is_valid_pos(r, c):
            return True
        
        # check next line
        for i in range(c-len(str(num))-1, c+1):
            if is_valid_pos(r+1, i):
                return True
        return False
    
def is_valid_pos(r, c):
    if r < 0 or r >= m or c < 0 or c >= n or lines[r][c] == '.':
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
                # check if valid then add to sum
                # print(f"{num=} {r=} {i=}")
                if is_valid(num, r, i):
                    # print(num)
                    total += num
                num = []
    # number could be end of line
    if num:
        i += 1
        num = int(''.join(num))
        # check if valid then add to sum
        # print(f"{num=} {r=} {i=}")
        if is_valid(num, r, i):
            # print(num)
            total += num
        num = []
        
print(f"Total is {total}")
    