
###### PART 1 ###########

file_path = '01.txt'  
total = 0
with open(file_path, 'r') as file:
    
    for line in file:
        
        processed_line = line.strip()  # Remove leading and trailing whitespace

        for i in range(len(processed_line)):
            if processed_line[i].isdigit():
                start = processed_line[i]
                break
        
        for i in range(len(processed_line)-1, -1, -1):
            if processed_line[i].isdigit():
                end = processed_line[i]
                break
            
        total += int(start) * 10 + int(end)

print(f"Final total is {total}")
# Final total is 55123

###### PART 2 ###########

threes = ['one', 'two', 'six']
fours = ['four', 'five', 'nine']
fives = ['three', 'seven', 'eight']

mapping = {'one': 1, 'two': 2, 'three': 3, 'four' : 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine' : 9}

file_path = '01.txt'  
total = 0
with open(file_path, 'r') as file:
    
    for line in file:
        
        processed_line = line.strip()  # Remove leading and trailing whitespace
        n = len(processed_line)
        for i in range(n):
            
            if processed_line[i].isdigit():
                start = processed_line[i]
                break
            elif i + 3 <= n and processed_line[i:i+3] in threes:
                start = mapping[processed_line[i:i+3]]
                break
            elif i + 4 <= n and processed_line[i:i+4] in fours:
                start = mapping[processed_line[i:i+4]]
                break
            elif i + 5 <= n and processed_line[i:i+5] in fives:
                start = mapping[processed_line[i:i+5]]
                break
                
        for i in range(n-1, -1, -1):
            if processed_line[i].isdigit():
                end = processed_line[i]
                break   
            elif i - 3 >= 0 and processed_line[i-2:i+1] in threes:
                end = mapping[processed_line[i-2:i+1]]
                break
            elif i - 4 >= 0 and processed_line[i-3:i+1] in fours:
                end = mapping[processed_line[i-3:i+1]]
                break
            elif i - 5 >= 0 and processed_line[i-4:i+1] in fives:
                end = mapping[processed_line[i-4:i+1]]
                break
                
        num = int(start) * 10 + int(end)
        total += num

print(f"Final total is {total}")
# Final total is 55260

