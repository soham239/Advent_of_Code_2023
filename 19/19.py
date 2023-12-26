f = open("19.txt").read().split("\n\n")
fs = f[0].split("\n")
flows = {}
for i in fs:
    k, v = i.split("{")
    v = v[:-1].split(",")
    flows[k] = v
items = f[1].split("\n")
def run(item):
    curr_flow = "in"
    while True:
        for i in flows[curr_flow]:
            if ":" in i: # condition
                cond, act = i.split(":")
                if ">" in cond:
                    a, b = cond.split(">")
                    if item[a] > int(b):
                        if act == "A":
                            return True
                        if act == "R":
                            return False
                        curr_flow = act
                        break
                if "<" in cond:
                    a, b = cond.split("<")
                    if item[a] < int(b):
                        if act == "A":
                            return True
                        if act == "R":
                            return False
                        curr_flow = act
                        break
            if i == "A":
                return True
            if i == "R":
                return False
            curr_flow = i

r = 0
for i in items:
    item = {}
    for j in i[1:-1].split(","):
        k, v = j.split("=")
        item[k] = int(v)
    if run(item):
        r += sum(item.values())
print(r)