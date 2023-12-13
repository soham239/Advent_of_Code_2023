# From: https://topaz.github.io/paste/#XQAAAQAvAQAAAAAAAAA4HMAC0B3AtL+oWviBxctH86JJ/6PHrH/ibLmvcCigiNSr3DJj/8ZvYRMK4yAj3KqAAi0HpH+1HI3c477ShjEEy5eU0rJZ5XPMYjUa7KUUSMAW1drkZO07jdwAFDkc4bNsMoNxYUsKIVSpdlovqUPejkc8NpWtBAgIWd7/9ZC4/XSwnbMYcblPFtJMKIF6yJqiVrhsUCTxX5zJZd/K0lmHVrZ/8Hi1ih/6gOHGvfXUkst4D1Vh+XV6LhD8OqPlRM7DQNvM8SKMBsBnnuE+BBYeFTWIuJIFP//B2RkA

ps = list(map(str.split, open('13.txt').read().split('\n\n')))

def f(p):
    for i in range(len(p)):
        if sum(c != d for l,m in zip(p[i-1::-1], p[i:])
                      for c,d in zip(l, m)) == s: return i
    else: return 0

for s in 0,1: print(sum(100 * f(p) + f([*zip(*p)]) for p in ps))