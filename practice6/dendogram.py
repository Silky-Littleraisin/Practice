#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import networkx as nx
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

G = nx.karate_club_graph()

matrix = nx.to_numpy_matrix(G)
# 階層的クラスタリングをする
z = linkage(matrix, method='ward', metric = 'euclidean')

plt.figure(figsize=(8, 7))
# デンドログラムを描画する
dendrogram(z, leaf_rotation=0)
plt.show()