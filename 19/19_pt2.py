from copy import deepcopy

f = open("sample.txt").read().split("\n\n")
fs = f[0].split("\n")
flows = {}
for i in fs:
    k, v = i.split("{")
    v = v[:-1].split(",")
    flows[k] = v

def sz(rng):
    r = 1
    for i in rng.values():
        r *= i[1] - i[0] + 1
    return r

def run(rng, flow):
    r = 0
    print(rng, flow)
    for i in flows[flow]:
        if ":" in i: # condition
            cond, act = i.split(":")
            if ">" in cond:
                a, b = cond.split(">")
                new_rng = deepcopy(rng)
                if new_rng[a][1] > int(b):
                    new_rng[a][0] = max(new_rng[a][0], int(b)+1)
                    if act == "A":
                        r += sz(new_rng)
                    elif act != "R":
                        r += run(new_rng, act)
                    rng[a][1] = min(rng[a][1], int(b))
            if "<" in cond:
                a, b = cond.split("<")
                new_rng = deepcopy(rng)
                if new_rng[a][0] < int(b):
                    new_rng[a][1] = min(new_rng[a][1], int(b)-1)
                    if act == "A":
                        r += sz(new_rng)
                    elif act != "R":
                        r += run(new_rng, act)
                    rng[a][0] = max(rng[a][0], int(b))
        else:
            if i == "A":
                r += sz(rng)
            elif i != "R":
                r += run(rng, i)
    return r

print(run({"x":[1,4000], "m":[1,4000], "a":[1,4000], "s":[1,4000]}, "in"))