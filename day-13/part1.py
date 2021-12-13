"""https://adventofcode.com/2021/day/13"""

import re

data = open("day-13/input", "r", encoding="utf-8").read()
coords_section, folds_section = data.split("\n\n")
coords = {tuple(map(int, c.split(","))) for c in coords_section.splitlines()}
folds = [re.match(r"fold along (x|y)=(\d+)", f).groups() for f in folds_section.splitlines()]
folds = [(a, int(v)) for a, v in folds]

for axis, v in folds[0:1]:
    if axis == 'y':
        coords = {(x, y) for x, y in coords if y < v} | {(x, v - (y - v)) for x, y in coords if y >= v}
    elif axis == 'x':
        coords = {(x, y) for x, y in coords if x < v} | {(v - (x - v), y) for x, y in coords if x >= v}

print(len(coords))
# 724
