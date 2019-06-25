#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()  # 無向グラフ
# エッジファイルを読み込む
with open("karate.edges") as f:
    for line in f:
        col = line.rstrip().split("\t")
        G.add_edge(col[1], col[0])  # グラフにエッジを追加

plt.figure(figsize=(8, 7))  # 画像サイズ(x, y)[inch]
nx.draw_networkx(
    G,
    pos=nx.circular_layout(G),        # 円状に並べる
    with_labels=True,                 # ノードにラベルを描画
    node_color="Skyblue",             # ノードの色
    node_size=700,                    # ノードの大きさ
    width=0.5,                        # エッジの太さ
    edge_color="0.5",                 # エッジの色
    edgecolors="0.7",                 # ノードの枠線の色
    linewidths=0.5                    # ノードの枠線の太さ
)
plt.axis('off') # 軸を表示しない
plt.show()
