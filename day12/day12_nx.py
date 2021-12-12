from day12_data import data
import networkx as nx
import matplotlib.pyplot as plt

def col(node):
    if node == 'start':
        return 'green'
    elif node == 'end':
        return 'red'
    elif node.islower():
        return 'grey'

graph = nx.Graph()

for start, finish in data:
    if start not in graph:
        graph.add_node(start, color=col(start))
    if finish not in graph:
        graph.add_node(finish, color = col(finish))

    graph.add_edge(start,finish)

nx.draw(graph,pos = nx.layout.spring_layout(graph,pos={'start':(0,1), 'end':(0,-1)}, fixed=['start','end']), with_labels = True, font_weight='bold')
plt.show()