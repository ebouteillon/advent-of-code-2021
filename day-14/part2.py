"""https://adventofcode.com/2021/day/14#part2"""

from collections import Counter

data = open("day-14/input", "r", encoding="utf-8").read().splitlines()
template = data[0]
rules = {a: b for a, b in [x.split(" -> ") for x in data[2:]]}

# Count each pair of letters in the template
pairs = Counter([template[i : i + 2] for i in range(len(template) - 1)])

# Update pairs count at each step as per rules
for _ in range(40):
    new_pairs = Counter()
    for p, v in pairs.items():
        if p in rules:
            c = rules[p]
            new_pairs[p[0] + c] += v
            new_pairs[c + p[1]] += v
        else:
            new_pairs[p] += pairs[p]
    pairs = new_pairs

# Count letters at the final step by counting first letter of each pairs,
# plus the final letter which is invariant during the whole process
count = Counter()
for p, v in pairs.items():
    count[p[0]] += v
count[template[-1]] += 1

print(count.most_common()[0][1] - count.most_common()[-1][1])
