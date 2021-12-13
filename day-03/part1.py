"""https://adventofcode.com/2021/day/3"""

data = open('day-03/input', 'r', encoding='utf-8').read().splitlines()

N = len(data[0])

gamma = 0
epsilon = 0

for n in range(N):
    count0 = sum(1 for line in data if line[n] == '0')
    count1 = len(data) - count0
    gamma *= 2
    epsilon *= 2
    if count0 < count1:
        gamma += 1
    else:
        epsilon += 1

print(gamma * epsilon)
# 3374136
