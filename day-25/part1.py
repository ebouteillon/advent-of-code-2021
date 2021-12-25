"""https://adventofcode.com/2021/day/25"""

import numpy as np

data = open("day-25/input", "r", encoding="utf-8").read().splitlines()
mapping = {'.': 0, '>': 1, 'v': 2}
board1 = np.array([[mapping[x] for x in line] for line in data])

count, moved = 0, True
while moved:
    before = board1.copy()

    board2 = np.zeros_like(board1)
    board2[(np.roll(board1, 1, axis=1) == 1) & (board1 == 0)] = 1
    board2[(board1 == 1) & (np.roll(board1, -1, axis=1) != 0)] = 1
    board2[board1 == 2] = 2

    board1 = np.zeros_like(board2)
    board1[(np.roll(board2, 1, axis=0) == 2) & (board2 == 0)] = 2
    board1[(board2 == 2) & (np.roll(board2, -1, axis=0) != 0)] = 2
    board1[board2 == 1] = 1

    count += 1
    moved = not np.array_equal(before, board1)
print(count)
