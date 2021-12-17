"""https://adventofcode.com/2021/day/15#part2"""

import networkx as nx
import numpy as np

data = open("day-15/input", "r", encoding="utf-8").read()
df = np.array([[int(x) for x in line] for line in data.splitlines()])
row = np.hstack([(df + i - 1) % 9 + 1 for i in range(5)])
df = np.vstack([(row + i - 1) % 9 + 1 for i in range(5)])
w, h = df.shape
G = nx.grid_2d_graph(w, h, create_using=nx.DiGraph())
nx.set_edge_attributes(G, {e: df[e[1][0], e[1][1]] for e in G.edges()}, "cost")
print(nx.shortest_path_length(G, source=(0, 0), target=(w - 1, h - 1), weight="cost"))
