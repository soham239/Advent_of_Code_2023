file_path = '02.txt'  

total = 0

blue_max = 14
green_max = 13
red_max = 12

with open(file_path, 'r') as file:
    
    for line in file:
        id = int(line.split(':')[0][4:])
        games = line.strip().split(':')[1].split(';')
        
        valid = True
        for bunch in games:
            
            for game in bunch.split(','):

                if 'blue' in game and int(game[:-4]) > blue_max:
                    valid = False
                    break
                
                if 'red' in game and int(game[:-3]) > red_max:
                    valid = False
                    break
                
                if 'green' in game and int(game[:-5]) > green_max:
                    valid = False
                    break
        
        if valid:
            total += id

print(f"Total is {total}")
              
####### PART 2 #############

file_path = '02.txt'  

total = 0

with open(file_path, 'r') as file:
    
    for line in file:
        
        blue_max = 0
        red_max = 0
        green_max = 0
        
        id = int(line.split(':')[0][4:])
        games = line.strip().split(':')[1].split(';')
        
        valid = True
        for bunch in games:
            
            for game in bunch.split(','):

                if 'blue' in game:
                    blue_max = max(blue_max, int(game[:-4]))

                if 'red' in game:
                    red_max = max(red_max, int(game[:-3]))
                
                if 'green' in game:
                    green_max = max(green_max, int(game[:-5]))
        
        total += green_max * blue_max * red_max
 
print(f"Total is {total}")