#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import networkx as nx

G = nx.karate_club_graph()
print("ノード数", nx.number_of_nodes(G))
print("エッジ数", nx.number_of_edges(G))
print("ノード一覧", G.nodes)
print("エッジ一覧", G.edges)
