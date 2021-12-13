"""https://adventofcode.com/2021/day/8#part2"""

data = open("day-08/input", "r").read().splitlines()
data = [x.split('|') for x in data]
data = [(i.split(), o.split()) for i, o in data]


def intersect(a, b):
    return len(set(a).intersection(b))


total = 0
for d in data:

    # Find wires representations of 1, 4, 7, 8 based on number of wires used
    for n in d[0]:
        n = ''.join(sorted(n))
        length = len(n)

        # 1 has 2 segments
        if length == 2:
            one = n
        # 4 has 4 segments
        elif length == 4:
            four = n
        # 7 has 3 segments
        elif length == 3:
            seven = n
        # 8 has 7 segments
        elif length == 7:
            eight = n

    # Deduce others digits only by comparing wires with representation of 1, 4, 7, 8
    for n in d[0]:
        n = ''.join(sorted(n))
        length = len(n)

        # 0, 6 and 9 have 6 segments
        if length == 6:
            if intersect(n, four) == 4:
                nine = n
            elif intersect(n, one) == 2:
                zero = n
            else:
                six = n

        # 2, 3 and 5 have 5 segments
        if length == 5:
            if intersect(n, one) == 2:
                three = n
            elif intersect(n, four) == 2:
                two = n
            else:
                five = n

    match = {
        zero: '0',
        one: '1',
        two: '2',
        three: '3',
        four: '4',
        five: '5',
        six: '6',
        seven: '7',
        eight: '8',
        nine: '9'
    }

    value = ''.join(match[''.join(sorted(x))] for x in d[1])
    total += int(value)

print(total)
# 1043697
