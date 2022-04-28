
class graphBasic():

    def __init__(self, size):
        self.array = []
        for i in range(size):
            temp = []
            for j in range(size):
                temp.append(0)
            self.array.append(temp)



    def addEdge(self, u, v):
        self.array[u][v] = 1
        self.array[v][u] = 1

    def display(self):
        print(self.array)
        return self.array





newgraph = graphBasic(4)

newgraph.addEdge(0, 1)
newgraph.addEdge(1, 2)
newgraph.addEdge(2, 3)
newgraph.addEdge(3, 0)

ans = newgraph.display()




