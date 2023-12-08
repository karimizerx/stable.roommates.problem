import networkx as nx
import matplotlib.pyplot as plt
              
members = ["A", "B", "C", "D" , "E", "F"]

G = nx.MultiDiGraph(format='png', directed=True)

for e in members:
    G.add_node(e)
    for l in members:
        if (not (e==l)):
            G.add_edge(e,l)
        
pos={
    "A" : (0.866,0),
    "B" : (0,0.5),
    "C" : (0,1.5),
    "D" : (0.866,2),
    "E" : (1.732,1.5),
    "F" : (1.732,0.5)
}

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, connectionstyle="arc3,rad=0.08")
nx.draw_networkx_labels(G, pos)
plt.show()