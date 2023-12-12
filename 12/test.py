# https://topaz.github.io/paste/#XQAAAQAZAgAAAAAAAAAzHIoib6poHLpewxtGE3pTrRdzrponKxDhfDpmqUbmwK1em8UhjnLeDrUM3bsKz4hSbgD7CUhJSBIGPN/l9tGeHau3I37QurKdTO+AzFTwLaQEp62YuSRp9m4HPF1MaOeRol+9iwXwktNbFbjaci7WB7gl3yN0Ko6zYrAhg9YIV4139KA2R72kur6VJfxzwYxeXli0I0PMRVKqqQLbnRKdjCj+k+TSxNeLJGVG1Vde77TKkd3XZh+jB6kfhmJau7Dy0fi9BUW4vLcz35iMQxKtY9Ay1U5oah2p/l9vVab0jesk2HFqm1mCpLZK00R+WJ2aOULpOT54heKkCxsPQ+OrD7GOGjC2gHDj38YqOttmDxGxTwwAjxO4EkEbv79HBXjbIfUzaACxBa8VP/8tTwsA

from functools import cache

def f(line):
    P, N = line.split()
    P = '?'.join([P] * 5)
    N = [int(n) for n in N.split(',')] * 5

    @cache
    def dp(p, n):
        
        if p >= len(P): return n == len(N)

        r = 0
        
        if P[p] in '.?': r += dp(p+1, n)

        if P[p] in '#?' and n < len(N) and \
            (p + N[n] <= len(P) and '.' not in P[p:p+N[n]]) and \
            (p + N[n] == len(P) or  '#' not in P[p+N[n]]):
            r += dp(p+N[n]+1, n+1)

        return r

    return dp(0, 0)

print(sum(map(f, open('12.txt'))))