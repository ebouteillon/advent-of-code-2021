"""https://adventofcode.com/2021/day/20"""

import numpy as np
from scipy.signal import convolve2d


def enhance(times):
    data = open("day-20/input", "r", encoding="utf-8").read().splitlines()
    algo = [int(x == "#") for x in data[0]]
    img = np.array([[int(x == "#") for x in y] for y in data[2:]])

    matrix = np.array([[1, 2, 4], [8, 16, 32], [64, 128, 256]])
    fillvallue = 0
    for _ in range(times):
        idx = convolve2d(img, matrix, fillvalue=fillvallue)
        img = np.vectorize(lambda x: algo[x])(idx)
        fillvallue = algo[0] if fillvallue == 0 else algo[511]
    print(img.sum())


# part 1
enhance(2)

# part 2
enhance(50)
