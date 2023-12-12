
file_path = '12.txt'

# Open and read the file content
with open(file_path, 'r') as file:
    file_content = file.read()
    
# Split the file content into lines
lines = file_content.strip().split('\n')
total = 0
for line in lines:
    pattern = line.split(' ')[0]
    counts = [int(i) for i in line.split(' ')[1].split(',')]
    # print(f"{pattern=} {counts=}")
    
    # 0 is a placeholder for end limiter
    def dp(i, cnts):
        
        # Base case
        if len(cnts) > len(counts) + 1:
            return 0

        
        # print(f"{cnts=} {counts=}")
        # Prune the results that are impossible - part 2 important
        # if cnts[:-1] != counts[:len(cnts)-1]:
        #     return 0
        
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
             
    total += dp(0, [0])

print(f"Ans is {total}")