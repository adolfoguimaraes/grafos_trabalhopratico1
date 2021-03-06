import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node('v1')
G.add_node('v2')
G.add_node('v3')
G.add_node('v4')
G.add_node('v5')

G.add_edge('v1','v2')
G.add_edge('v2','v3')
G.add_edge('v3','v4')
G.add_edge('v4','v5')
G.add_edge('v5','v1')
G.add_edge('v2','v4')

print(G.number_of_nodes())
print(G.number_of_edges())
print(G.nodes)
print(G.edges)

plt.figure(2)
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()
