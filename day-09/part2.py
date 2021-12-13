"""https://adventofcode.com/2021/day/9#part2"""

import numpy as np
from skimage.measure import label, regionprops

df = np.array([list(map(int, [c for c in line])) for line in open("day-09/input", "r", encoding="utf-8").read().splitlines()])
print(np.prod(sorted([r.area for r in regionprops(label(df < 9, connectivity=1))])[-3:]))
# 1100682
