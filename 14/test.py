# From: https://topaz.github.io/paste/#XQAAAQA+BgAAAAAAAAA0m0pnuFI8c/fBNAqG6qhqaa80vAO7Zo0MJsDq5oR1nT8qh9Fl1Ro8Nx+h+Chcju+e7yW/uEzpsNdhApcVzcjF1fBBimB7hWuVbNdAhv+DsZY7pWnofrJW2T9ksyrpQL8RPgRezN9iQGk6wdrsGNjhF5lTAb8DJVwQHtFIMOw9TefUE03Hp/fzIbsQ+xXwGg6/qR6JrrobVJUf9Kdz+rtCXxX58bX6GpPtKn6la0qguc0sCtVzcwyl6JiO7qvGJLM/Fy+pfzTlNKSabX83t4lYIk+3fBBoZ7TVM/PBjPQ5ECGJHlYUUDE61syy7C9yZD0IhUvgVtUiGK78tuFtmjlGbh5vUl678LMPXepMHUocwdI6auHHdEUXu0YGlU+ZSWeALFzZeQvVuKCtdqvVFlHoujYbcWZGuIUr7+6ODZNpYspJW+sSoKstygdUIIWjJ/tOpi6GZELQGrrBZKOhdudQHgqhWqSRn/PYcS9b9Tp1se/Ay6lGU6nD0NXMszzJ0Zyu6wb/lBW7UiyRkjYOipmyTH7s1UWUHmGk6FT47psoeBloBG/ivwoo5mZrk2K2q1IYZY+8l3IjtVcYq+l372ecRrxPcyrch2EGlYD0fQ2DzfXDownIrxepDjYmj000RmEuzFGPaICw9euevFFrP2/21JgU1xXcOBkw5u21r5dgpdnwayUZ4sb2Qrl+UBqZqWTwrgwBXa2SHVyvufl8AMiQa2x9cAefXHdIO4wvmK0GUtqiaPfpqJjCqHibQtnnsACryZlmv4Bwnx/zbaLT1yQaa4LL7T/OZP5WMWHKC9yTOyP0NkxB/+ziIN4=

import sys

def Score(G):
    score = 0
    for n, g in enumerate(G[::-1], start=1):
        score += n * str(g).count('O')
    return score

def Cycle(G):
    G = TiltUp(G)
    G = TiltLeft(G)
    G = TiltDown(G)
    G = TiltRight(G)
    return G

def TiltLeft(G):
    for n, i in enumerate(G):
        i = list(i)
        for x in range(len(i)):
            if i[x] != 'O':
                continue
            at = x
            to = at - 1
            while to >= 0:
                if to >= 0 and i[to] == '.':
                    i[at] = '.'
                    i[to] = 'O'
                else:
                    break
                to -= 1
                at -= 1
        G[n] = i
    return G

def TiltUp(g):
    I = list(zip(*g))
    I = TiltLeft(I)
    return list(zip(*I))

def TiltDown(g):
    g = g[::-1]
    g = TiltUp(g)
    g = g[::-1]
    return g

def TiltRight(g):
    g = [x[::-1] for x in g]
    g = TiltLeft(g)
    g = [x[::-1] for x in g]
    return g

file_path = '14.txt'
with open(file_path, 'r') as file:
    G = file.read().strip().split('\n')
# G = sys.stdin.read().strip().split('\n')
G1 = G.copy()
G1 = TiltUp(G1)
print(Score(G1))

Scores = set()
T = ''.join([''.join(x) for x in G])
Scores.add(Score(T))

again = True
times = 0
first = None
rep = None
G2 = G.copy()
while True:
    G2 = Cycle(G2)

    times += 1
    T = ''.join([''.join(x) for x in G2])
    if T in Scores:
        if again == True:
            again = False
            Scores = set()
            first = times
        else:
            rep = times
            break
    Scores.add(T)

T = 1000000000
T -= first
T %= (rep - first)

for _ in range(T+first):
    G = Cycle(G)

print(Score(G))