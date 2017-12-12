from sys import stdin
class Node:
    def __init__(self, adj):
        self.adj = adj
        self.visits = 0
ids = [line.strip().split(' <-> ') for line in stdin.readlines()]
graph = {}
for prog in ids:
    children = set(prog[1].split(', '))
    if prog[0] not in graph:
        graph[prog[0]] = Node(children)
    else:
        graph[prog[0]].adj.update(children)
    for child in children:
        if child not in graph:
            graph[child] = Node({prog[0]})
        else:
            graph[child].adj.update({prog[0]})
count = 0
start = graph['0']
def search(start):
    for node in start.adj:
        comp = graph[node]
        if comp.visits < 1:
            comp.visits += 1
            search(graph[node])
search(graph['0'])
for key in graph.keys():
    if graph[key].visits > 0:
        count += 1
print(count)
