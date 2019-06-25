#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()

# 次数のヒストグラムを得る
degree_sequence = nx.degree_histogram(G)
x = range(len(degree_sequence))  # 0 .. 最大次数の配列
plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
# 棒グラフで描画
plt.bar(
    x,
    degree_sequence,
    tick_label=x
)
plt.show()