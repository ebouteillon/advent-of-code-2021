"""https://adventofcode.com/2021/day/1#part2"""

data = open('day-01/input', 'r', encoding='utf-8').read().splitlines()
depths = [int(x) for x in data]

# We don't need to sum the elements, because comparing:
#  depths[i] + depths[i+1] + depths[i+2] < depths[i+1] + depths[i+2] + depths[i+3]
# has the same resuts as comparing:
#  depths[i] < depths[i+3]

increases = sum(x < y for x, y in zip(depths, depths[3:]))
print(increases)
# 1378
