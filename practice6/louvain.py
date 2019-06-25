#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import networkx as nx
import matplotlib.pyplot as plt
import community

G = nx.karate_club_graph()
partition = community.best_partition(G)
size = len(set(partition.values()))
print("クラスタサイズ:", size)

plt.figure(figsize=(8, 7))
nx.draw_networkx(
    G,
    pos=nx.spring_layout(G, seed=1),
    with_labels=True,
    node_color=list(partition.values()),
    cmap=plt.get_cmap("tab20"),
    node_size=700,
    width=0.5,
    edge_color="0.5",
    edgecolors="0.5",
    linewidths=0.5
)
plt.axis('off')
plt.show()
