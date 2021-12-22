"""https://adventofcode.com/2021/day/21"""


class Die:
    def __init__(self, sides=100):
        self.sides = sides
        self.value = 0
        self.rolled = 0

    def roll(self):
        self.rolled += 1
        self.value = self.value % self.sides + 1
        return self.value


data = open("day-21/input.txt", "r", encoding="utf-8").read().splitlines()
position_1 = int(data[0].split(" ")[-1])
position_2 = int(data[1].split(" ")[-1])
score_1, score_2 = 0, 0

die = Die()
while True:
    position_1 = (position_1 + die.roll() + die.roll() + die.roll() - 1) % 10 + 1
    score_1 += position_1
    if score_1 >= 1000:
        print(score_2 * die.rolled)
        exit()
    position_2 = (position_2 + die.roll() + die.roll() + die.roll() - 1) % 10 + 1
    score_2 += position_2
    if score_2 >= 1000:
        print(score_1 * die.rolled)
        exit()
