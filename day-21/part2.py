"""https://adventofcode.com/2021/day/21#part2"""


from dataclasses import dataclass
from functools import lru_cache
import numpy as np


@dataclass(eq=True, frozen=True)
class State:
    position1: int
    position2: int
    score1: int
    score2: int
    player_turn: int


# Sum of the 3 dice rolls: possible ways to get
dicesum_odds = (
    (3, 1),
    (4, 3),
    (5, 6),
    (6, 7),
    (7, 6),
    (8, 3),
    (9, 1),
)


def new_position(position, dice_sum):
    return (position + dice_sum - 1) % 10 + 1


@lru_cache(maxsize=None)
def count_wins(s: State):
    if s.score1 >= 21:
        return np.array((1, 0))
    if s.score2 >= 21:
        return np.array((0, 1))

    wins = np.array((0, 0))
    for dice_sum, odds in dicesum_odds:
        if s.player_turn == 1:
            pos = new_position(s.position1, dice_sum)
            new_s = State(pos, s.position2, s.score1 + pos, s.score2, 2)
        else:
            pos = new_position(s.position2, dice_sum)
            new_s = State(s.position1, pos, s.score1, s.score2 + pos, 1)
        wins += count_wins(new_s) * odds

    return wins


data = open("day-21/input.txt", "r", encoding="utf-8").read().splitlines()
position1 = int(data[0].split(" ")[-1])
position2 = int(data[1].split(" ")[-1])
print(max(count_wins(State(position1, position2, 0, 0, 1))))
