#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
plt.figure(figsize=(7, 6))
nx.draw_networkx(
    G,
    pos=nx.random_layout(G), # ランダムに配置する
    with_labels=True,
    node_color="Skyblue",
    node_size=700,
    width=0.5,
    edge_color="0.5",
    edgecolors="0.7",
    linewidths=0.5
)
plt.axis('off')
plt.axis('off')
plt.show()