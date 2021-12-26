"""https://adventofcode.com/2021/day/24"""


import z3

# Values from "input" file
V = [
    [1, 12, 1],
    [1, 12, 1],
    [1, 15, 16],
    [26, -8, 5],
    [26, -4, 9],
    [1, 15, 3],
    [1, 14, 2],
    [1, 14, 15],
    [26, -13, 5],
    [26, -3, 11],
    [26, -7, 7],
    [1, 10, 1],
    [26, -6, 10],
    [26, -8, 3],
]


def Solver():
    solver = z3.Optimize()
    var = [z3.Int(f"s_{i}") for i in range(14)]
    for i in range(14):
        solver.add(var[i] >= 1, var[i] <= 9)

    z = 0
    for i in range(14):
        x = z % 26
        z /= V[i][0]
        z = z3.If(x + V[i][1] != var[i], z * 26 + var[i] + V[i][2], z)
    solver.add(z == 0)
    return solver, var


# Part 1
solver, var = Solver()
solver.maximize(sum([v * 10 ** (13 - i) for i, v in enumerate(var)]))
solver.check()
m = solver.model()
print([m[x] for x in var])


# Part 2
solver, var = Solver()
solver.minimize(sum([v * 10 ** (13 - i) for i, v in enumerate(var)]))
solver.check()
m = solver.model()
print([m[x] for x in var])
