file_path = '09.txt'

# Open and read the file content
with open(file_path, 'r') as file:
    file_content = file.read()
    
# Split the file content into lines
lines = file_content.strip().split('\n')

def get_next_value(seq):
    last = []
    while not all(value == 0 for value in seq):
        out = []
        last.append(seq[-1])
        for i in range(len(seq)-1):
            out.append(seq[i+1]-seq[i])
        seq = out
    
    res = 0
    for num in last[::-1]:
        res += num
    
    return res

total = 0
for line in lines:
    seq = [int(num) for num in line.split()]
    total += get_next_value(seq)
    
print(f"Ans is {total}")