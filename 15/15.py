from collections import OrderedDict

def calculate(key):
    val = 0
    for c in key:
        val += ord(c)
        val *= 17
        val %= 256
    return val

print("Part 1")
print(sum(list(map(calculate, open('15.txt').read().split(',')))))

lenses = [OrderedDict() for _ in range(256)]

def position(key):
    # Calculate hash
    if '-' in key:
        box = calculate(key[:-1])
    elif '=' in key:
        box = calculate(key.split('=')[0])

    # Manage lens in box
    if '-' in key:
        lenses[box].pop(key[:-1], None)
    elif '=' in key:
        lenses[box][key.split('=')[0]] = key.split('=')[1]

def total(lenses):
    ans = 0
    for j, box in enumerate(lenses, start=1):
        i = 1
        for k, v in box.items():
            # print(f"{j=} {i=} {v=} {box=}")
            ans += j * i * int(v)
            i += 1
    return ans
        
# Put in labels   
list(map(position, open('15.txt').read().split(',')))

print("Part 2")
print(total(lenses))

