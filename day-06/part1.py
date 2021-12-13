"""https://adventofcode.com/2021/day/6"""

import numpy as np

data = open("day-06/input", encoding='utf-8').read()
df = np.array([int(x) for x in data.split(",")])

for day in range(80):
    df -= 1
    new = np.sum(df < 0)
    df = np.where(df < 0, 6, df)
    if new:
        df = np.hstack([df, np.full(new, 8)])
    print(f"After {day+1} days:", df)

print(df.shape)
# 362346
