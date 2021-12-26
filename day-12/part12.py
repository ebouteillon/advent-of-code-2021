"""https://adventofcode.com/2021/day/12"""

data = open("day-12/input.txt", "r", encoding="utf-8").read()
lst = [line.split("-") for line in data.splitlines()]
edges = [[a, b] for a, b in lst if a != "end" and b != "start"]
edges += [[b, a] for a, b in lst if a != "start" and b != "end"]


def find_path_r(current_path, found_paths, repeat):
    current_node = current_path[-1]
    if current_node == "end":
        found_paths.append(current_path)
        return
    for edge in edges:
        if edge[0] == current_node:
            if edge[1].isupper() or edge[1] not in current_path:
                find_path_r(current_path + [edge[1]], found_paths, repeat)
            elif edge[1].islower() and edge[1] in current_path and repeat:
                find_path_r(current_path + [edge[1]], found_paths, False)


def find_paths(repeat):
    """Find the all the paths from start to the end node"""
    found_paths = []
    find_path_r(["start"], found_paths, repeat)
    return found_paths


print(len(find_paths(False)))  # Part 1
print(len(find_paths(True)))  # Part 2
