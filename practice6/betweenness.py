#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
# 媒介中心性の計算
bc = nx.betweenness_centrality(G)

plt.figure(figsize=(14,8))
nx.draw_networkx(
    G,
    pos=nx.spring_layout(G, seed=1),
    with_labels=True,
    node_color=list(bc.values()),
    cmap=plt.cm.Blues,
    vmax=0.7,
    node_size=[10000*v for v in bc.values()],
    width=0.5,
    edge_color="0.5",
    edgecolors="0.5",
    linewidths=0.5
)
plt.axis('off')
plt.show()