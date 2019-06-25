#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
plt.figure(figsize=(7, 6))
nx.draw_networkx(
    G,
    pos=nx.spring_layout(G, seed=1),  # ばねモデルで位置を決める
    with_labels=True,                 #   位置はランダムで変わるため
    node_color="Skyblue",             #   seed=1でランダムの種を指定
    node_size=700,
    width=0.5,
    edge_color="0.5",
    edgecolors="0.7",
    linewidths=0.5
) 
plt.axis('off')
plt.show()