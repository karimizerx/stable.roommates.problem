import networkx as nx
import matplotlib.pyplot as plt
       
set1 = ["A", "B", "C", "D"]
set2 = ["1", "2", "3", "4"]

G = nx.MultiDiGraph(format='png', directed=True)

for element in set1:
    G.add_node(element)
    for vertex in set2:
        G.add_node(vertex)
        G.add_edge(element, vertex)
        G.add_edge(vertex, element)
        
pos={
    "A" : (1,0),
    "B" : (1,2),
    "C" : (0,1),
    "D" : (2,1),
    "1" : (2,0),
    "2" : (2,2),
    "3" : (0,2),
    "4" : (0,0)
}

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, connectionstyle="arc3,rad=0.1")
nx.draw_networkx_labels(G, pos)
plt.show()