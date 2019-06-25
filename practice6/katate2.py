#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import networkx as nx

G = nx.karate_club_graph()
for edge in G.edges:
    print(edge[0], edge[1], sep="\t")
