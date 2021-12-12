from day12_data import data

class Node:
    def __init__(self, node) -> None:
        self.connectedNodes = {}
        self.identifier = node
        self.start = node == 'start'
        self.end = node == 'end'
        self.small = node.islower()
    
    def addNodeConnection(self,node):
        self.connectedNodes[node.identifier] = node
        node.connectedNodes[self.identifier] = self

paths = 0
def traverse(node, traversed):
    global paths
    # traversed.add(node.identifier)
    if node.end:
        paths += 1
        return
    
    for k,n in node.connectedNodes.items():
        if n.small and k in traversed:
            continue
        traverse(n,{*traversed, node.identifier})


nodes = {}
startNode = None

for start, finish in data:
    if start not in nodes:
        nodes[start] = Node(start)
        if start == 'start':
            startNode = nodes[start]
    if finish not in nodes:
        nodes[finish] = Node(finish)
        if finish == 'start':
            startNode = nodes[finish]

    nodes[start].addNodeConnection(nodes[finish])


traverse(startNode, set())
print(paths)
