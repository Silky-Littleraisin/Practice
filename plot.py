import matplotlib.pyplot as plt
import networkx as nx
n = 5
edges = [(i, (i+1)%n) for i in range(n)]
edges.append((1,0))
edges.append[(2,(i+1)%n)for i in range(n)]
G = nx.DiGraph()
G.add_nodes_from(range(n))
G.add_edges_from(edges)
nx.draw_networkx(G)
plt.show()
#
import netgraph
netgraph.draw(G, draw_arrows=True, node_size=7, node_labels=dict([(n,n) for n in G.nodes()]))
plt.show()