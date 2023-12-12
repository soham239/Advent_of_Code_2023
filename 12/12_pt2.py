file_path = 'sample.txt'

# Open and read the file content
with open(file_path, 'r') as file:
    file_content = file.read()
    
# Split the file content into lines
lines = file_content.strip().split('\n')
total = 0
for l, line in enumerate(lines):
    # print(f"Line number: {l}")
    pattern = line.split(' ')[0]
    counts = [int(i) for i in line.split(' ')[1].split(',')]
    
    # print(f"{pattern=} {counts=}")
    
    # 0 is a placeholder for end limiter
    def dp(i, cnts):
        
        # Base case
        if len(cnts) > len(counts) + 1:
            return 0
        
        # Pruning calculations no need to do it 5 times
        # if len(cnts) > 2 * len(counts) // 5:
        #     n = 2 * len(counts) // 5
        #     return 1 if cnts[:n] == counts[:n] else 0
        
        # print(f"{cnts=} {counts=}")
        # Prune the results that are impossible - part 2 important
        if cnts[:-1] != counts[:len(cnts)-1]:
            return 0
        
        if i == len(pattern):
            # Reached end of string
            # All counts should tally
            if cnts[-1] == 0:
                cnts.pop()
            # print(f"{cnts=} {counts=}")
            return 1 if cnts == counts else 0
        
        if pattern[i] == '.':
            if cnts[-1] != 0:
                cnts.append(0)
            return dp(i+1, cnts)
        elif pattern[i] == '#':
            # start of a new set
            cnts[-1] = cnts[-1] + 1
            return dp(i+1, cnts)
        else:
            # question mark
            cnts2 = cnts.copy()
            # could be .
            if cnts[-1] != 0:
                cnts.append(0)
            dot = dp(i+1, cnts)
            # or could be #
            last = cnts2.pop()
            cnts2.append(last + 1)
            hash = dp(i+1, cnts2)
            return dot + hash
             
    res1 = dp(0, [0])
    # print(f"Res for 1x is {res1}")
    
    # For part 2
    pattern = '?'.join([pattern] * 2)
    counts = counts * 2
    res2 = dp(0, [0])
    # print(f"Res for 2x is {res2}")

    out =  res1 * ((res2//res1) ** 4)
    
    total += out
    # print(f"Out is {out}")
print(f"Ans is {total}")

# My Ans was 21829657531486
# Ans is actually - 51456609952403 - see code in test.py