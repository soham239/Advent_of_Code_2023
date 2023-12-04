file_path = '04.txt'  

total = 0

with open(file_path, 'r') as file:
    lines = []
    for line in file:
        nums = line.split(':')[1].split('|')
        win = nums[0].strip().split(' ')
        your = nums[1].strip().split(' ')
        
        win = [int(num) for num in win if num]
        your = [int(num) for num in your if num]

        count = 0
        for num in your:
            if num in win:
                count += 1
        if count:
            total += (2 ** (count-1))

print(total)