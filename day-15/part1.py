"""https://adventofcode.com/2021/day/15"""

import networkx as nx

data = open("day-15/input", "r", encoding="utf-8").read()
df = [[int(x) for x in line] for line in data.splitlines()]
w, h = len(df), len(df[0])
G = nx.grid_2d_graph(w, h, create_using=nx.DiGraph())
nx.set_edge_attributes(G, {e: df[e[1][0]][e[1][1]] for e in G.edges()}, "cost")
print(nx.shortest_path_length(G, source=(0, 0), target=(w - 1, h - 1), weight="cost"))
