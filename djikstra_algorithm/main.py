import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from heapq import heapify, heappush


def draw_graph(g):
    nx.draw(g, with_labels=True, node_size=2000, font_size=12, font_weight='bold')
    plt.show()

def djikstra(g, src, dist):
    infinity = float("inf")
    current = src
    visited = []
    cost = {
        'A': 0,
        'B': infinity,
        'C': infinity,
        'D': infinity,
        'E': infinity,
        'F': infinity,
    }
    pred = {
        'A': ['A'],
        'B': [],
        'C': [],
        'D': [],
        'E': [],
        'F': []
    }

    while current != dist:
        heap = []
        for neighbor in nx.neighbors(g, current):
            if neighbor not in visited:
                weight = g.get_edge_data(current, neighbor)["weight"]
                new_cost = cost[current] + weight
                if new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    pred[neighbor] = list(current)
                heappush(heap, (cost[neighbor], neighbor))

        visited.append(current)
        heapify(heap)
        current = heap[0][1]


    print("The shortest path from node ", src, " to ",dist," is:")
    stack = deque()
    l = dist
    stack.append(l)
    while l != src:
        pred_ = pred[l]
        l = pred_[0]
        stack.append(l)

    previous = "A"
    while stack:
        next = stack.pop()
        if previous != next:
            distance = g.get_edge_data(previous, next)["weight"]
            print(previous, "-->", next, "   /distance of: ", distance)
        previous = next

    print("With a Total distance of: ", cost[dist])




g = nx.Graph()

g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')

g.add_edge('A', 'B', weight = 2)
g.add_edge('A', 'C', weight = 4)
g.add_edge('C', 'B', weight = 3)
g.add_edge('D', 'B', weight = 8)
g.add_edge('C', 'D', weight = 2)
g.add_edge('F', 'D', weight = 22)
g.add_edge('C', 'E', weight = 5)
g.add_edge('E', 'D', weight = 11)
g.add_edge('E', 'F', weight = 1)



draw_graph(g)


src = input("What's your starting node: ")
while not g.has_node(src):
    src = input("Invalid starting node, choose an existing node: ")
dest = input("which node would you like to go to: ")
while not g.has_node(dest):
    dest = input("Invalid destination node, choose an existing node: ")


djikstra(g, src, dest)

