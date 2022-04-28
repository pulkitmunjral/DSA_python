# Following is Breadth First Traversal starting from vertex s

from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        stack = []

        # Mark the source node as
        # visited and enqueue it
        stack.append(s)
        visited[s] = True

        while stack:
            s = stack.pop()
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    stack.append(i)
                    visited[i] = True


# Driver code

# Create a graph given in
# the above diagram
g = Graph() # Total 5 vertices in graph
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(1, 4)
g.BFS(0)