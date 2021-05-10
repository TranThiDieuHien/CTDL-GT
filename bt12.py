# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:20:49 2021

@author: DUC-PC
"""

import networkx as nx
import matplotlib.pyplot as plt
#Đồ thị vô hướng
g = nx.DiGraph()
g.add_nodes_from([1,2,3,4,5])
g.add_edge(1,2)
g.add_edge(4,2)
g.add_edge(3,5)
g.add_edge(2,3)
g.add_edge(2,5)
g.add_edge(1,4)
g.add_edge(3,4)

nx.draw(g,with_labels=True, arrows=False)
plt.draw()
plt.show()