"""https://adventofcode.com/2021/day/11"""

import numpy as np
from scipy import signal

data = open("day-11/input", "r", encoding="utf-8").read().splitlines()
df = np.array([[int(x) for x in line] for line in data])

total = 0
for i in range(100):
    energy = np.ones_like(df)
    flashed = np.zeros_like(df)
    while np.any(energy.astype(bool)):
        df += energy
        flashing = np.logical_and((df > 9), np.logical_not(flashed))
        energy = signal.convolve(flashing, np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), mode='same')
        flashed = np.logical_or(flashed, flashing)
    df[flashed] = 0
    total += np.sum(flashed)
print(total)
# 1729
