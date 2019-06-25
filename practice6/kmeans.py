#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

G = nx.karate_club_graph()
matrix = nx.to_numpy_matrix(G)  # 行列へ変換
# k-meansの実行(クラスタ数2)
cluster = KMeans(n_clusters=2).fit_predict(matrix)
plt.figure(figsize=(8, 7))
nx.draw_networkx(
    G,
    pos=nx.spring_layout(G, seed=1),
    with_labels=True,
    node_color=cluster.tolist(),
    cmap=plt.get_cmap("Set3"),
    node_size=700,
    width=0.5,
    edge_color="0.5",
    edgecolors="0.5",
    linewidths=0.5
)
plt.axis('off')
plt.show()