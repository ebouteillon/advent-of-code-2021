"""https://adventofcode.com/2021/day/1"""

data = open('day-01/input', 'r', encoding='utf-8').read().splitlines()
depths = [int(x) for x in data]
increases = sum(x < y for x, y in zip(depths, depths[1:]))
print(increases)
# 1342
