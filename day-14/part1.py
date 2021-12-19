"""https://adventofcode.com/2021/day/14"""

from collections import Counter

data = open("day-14/input", "r", encoding="utf-8").read().splitlines()
template = data[0]
rules = {a: b for a, b in [x.split(" -> ") for x in data[2:]]}

for _ in range(10):
    new = ""
    for i in range(len(template) - 1):
        pair = template[i : i + 2]
        new += pair[0]
        if pair in rules:
            new += rules[pair]
    new += template[-1]
    template = new

count = Counter(template).most_common()
print(count[0][1] - count[-1][1])
