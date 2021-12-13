"""https://adventofcode.com/2021/day/3#part2"""

data = open('day-03/input', 'r', encoding='utf-8').read().splitlines()

N = len(data[0])


# Step 1: compute oxygen rating


def most_common(lst, position):
    count0 = sum(1 for x in lst if x[position] == '0')
    count1 = len(lst) - count0
    return '0' if count0 > count1 else '1'


def keep_most_common(d, position):
    v = most_common(d, position)
    return [x for x in d if x[position] == v]


lst = data.copy()
for i in range(N):
    if len(lst) <= 1:
        break
    lst = keep_most_common(lst, i)

oxygen = int(lst[0], 2)
print("oxygen", oxygen)


# Step 2: compute CO2 rating


def least_common(lst, position):
    count0 = sum(1 for x in lst if x[position] == '0')
    count1 = len(lst) - count0
    return '0' if count0 <= count1 else '1'


def keep_least_common(d, position):
    v = least_common(d, position)
    return [x for x in d if x[position] == v]


lst = data.copy()
for i in range(N):
    if len(lst) <= 1:
        break
    lst = keep_least_common(lst, i)

co2 = int(lst[0], 2)
print("co2", co2)

# Step 3: compute life support rating
print("life", co2 * oxygen)
# 4432698
