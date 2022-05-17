# Following is Breadth First Traversal starting from vertex s

from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, s):

        # Mark all the vertices as not visited
        visited = set()
        stack = []

        # Mark the source node as
        # visited and enqueue it
        stack.append(s)
        visited.add(s)

        while stack:
            s = stack.pop()
            print(s, end=" ")

            for i in self.graph[s]:
                if i not in visited:
                    stack.append(i)
                    visited.add(i)


# Driver code

# Create a graph given in
# the above diagram
g = Graph() # Total 5 vertices in graph
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.DFS(2)