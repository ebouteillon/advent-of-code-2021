"""https://adventofcode.com/2021/day/10#part2"""


def checker(line):
    stack = []
    for char in line:
        if char in '([{<':
            stack.append(char)
        elif char in ')':
            if stack.pop() != '(':
                return 3
        elif char in ']':
            if stack.pop() != '[':
                return 57
        elif char in '}':
            if stack.pop() != '{':
                return 1197
        elif char in '>':
            if stack.pop() != '<':
                return 25137
    return 0


data = open("day-10/input", "r", encoding="utf-8").read().splitlines()
print(sum(checker(line) for line in data))
# 299793
