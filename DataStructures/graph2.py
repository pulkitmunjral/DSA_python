
class graphBasic():

    def __init__(self, size):
        self.array = [[] for _ in range(size)]

    def addEdge(self, u, v):
        self.array[u].append(v)
        self.array[v].append(u)

    def display(self):
        print(self.array)
        return self.array


newgraph = graphBasic(4)

newgraph.addEdge(0, 1)
newgraph.addEdge(1, 2)
newgraph.addEdge(2, 3)
newgraph.addEdge(3, 0)

ans = newgraph.display()




