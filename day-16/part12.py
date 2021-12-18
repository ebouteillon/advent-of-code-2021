"""https://adventofcode.com/2021/day/16"""

from dataclasses import dataclass
from numpy import product


@dataclass
class Packet:
    version: int
    type_id: int
    literal: int
    length: int
    sub_packets: list


def parse_packet(bits, depth=0):
    version = int(bits[0:3], 2)
    type_id = int(bits[3:6], 2)
    position = 6

    # literal packet
    if type_id == 4:  # literal
        literal, is_last = 0, False
        while not is_last:
            is_last = bits[position] == "0"
            literal = (literal << 4) | int(bits[position + 1 : position + 5], 2)
            position += 5
        return Packet(version, type_id, literal, position, [])

    # operator packet
    length_type_id = int(bits[position], 2)
    position += 1
    if length_type_id == 0:  # total length in bits
        total_length = int(bits[position : position + 15], 2)
        position += 15
        length = 0
        sub_packets = []
        while length != total_length:
            sub = parse_packet(bits[position : position + total_length - length], depth + 1)
            sub_packets.append(sub)
            length += sub.length
            position += sub.length
        return Packet(version, type_id, 0, position, sub_packets)

    # number of sub-packets immediately contained
    number = int(bits[position : position + 11], 2)
    position += 11
    sub_packets = []
    for _ in range(number):
        sub = parse_packet(bits[position:], depth + 1)
        sub_packets.append(sub)
        position += sub.length
    return Packet(version, type_id, 0, position, sub_packets)


def add_versions(packets):
    total = 0
    for packet in packets:
        total += packet.version
        total += add_versions(packet.sub_packets)
    return total


def compute(p):
    if p.type_id == 4:
        return p.literal
    values = [compute(x) for x in p.sub_packets]
    if p.type_id == 0:
        return sum(values)
    elif p.type_id == 1:
        return product(values)
    elif p.type_id == 2:
        return min(values)
    elif p.type_id == 3:
        return max(values)
    elif p.type_id == 5:
        return int(values[0] > values[1])
    elif p.type_id == 6:
        return int(values[0] < values[1])
    elif p.type_id == 7:
        return int(values[0] == values[1])
    raise ValueError(f"Unknown type_id {p.type_id}")


data = open("day-16/input", "r", encoding="utf-8").read().strip()
bits = bin(int(data, 16))[2:].zfill(len(data) * 4)
packets = parse_packet(bits)

# part 1
print(add_versions([packets]))

# part2
print(compute(packets))
