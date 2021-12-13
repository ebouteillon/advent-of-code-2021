"""https://adventofcode.com/2021/day/2"""

data = open('day-02/input', 'r', encoding='utf-8').read().splitlines()
data = [x.split() for x in data]
commands = [(x[0], int(x[1])) for x in data]

h, d = 0, 0

for cmd, val in commands:
    if cmd == 'forward':
        h += val
    elif cmd == 'down':
        d += val
    elif cmd == 'up':
        d -= val
    else:
        raise ValueError('Invalid command')

print(h * d)
# 1962940
