"""https://adventofcode.com/2021/day/22"""

import re
import numpy as np

data = open("day-22/input.txt", "r", encoding="utf-8").read().splitlines()
regex = r"^(on|off) x=([0-9-]+)\.\.([0-9-]+),y=([0-9-]+)\.\.([0-9-]+),z=([0-9-]+)\.\.([0-9-]+)$"
steps = [re.match(regex, line).groups() for line in data]

DIM = 50
grid = np.zeros((2 * DIM + 1, 2 * DIM + 1, 2 * DIM + 1), dtype=int)

for toggle, x1, x2, y1, y2, z1, z2 in steps:
    x1, x2 = int(x1) + DIM, int(x2) + DIM
    y1, y2 = int(y1) + DIM, int(y2) + DIM
    z1, z2 = int(z1) + DIM, int(z2) + DIM
    if x1 >= 0 and x2 < 2 * DIM + 1 and y1 >= 0 and y2 < 2 * DIM + 1 and z1 >= 0 and z2 < 2 * DIM + 1:
        grid[x1:x2+1, y1:y2+1, z1:z2+1] = (toggle == "on")

print(np.sum(grid))
