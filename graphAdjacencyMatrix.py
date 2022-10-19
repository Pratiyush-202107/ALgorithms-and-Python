class AdjacencyMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjMatrix = [[0 for i in range(vertices)] for i in range(vertices)]

    def addEdge(self, v1, v2):
        if(v1 == v2):
            print(f"Both {v1} and {v2} are same vertices.")
            return
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print(f"There's no edge between vertex {v1} and {v2}.")
            return

        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    
    def printMatrix(self):
        for rows in self.adjMatrix:
            print(rows)

# Driver code
# sample = AdjacencyMatrix(3)
# sample.addEdge(0,1)
# sample.addEdge(1,2)

# sample.printMatrix()
#print(sample.adjMatrix)

vertices = int(input("Enter the number of vertices: "))
Graph = AdjacencyMatrix(vertices)

for rows in range(vertices):
    row = input(f"Enter row {rows + 1}: ")
    row = row.split(" ")
    row = [int(item) for item in row]
    for i in range(vertices):
        if row[i] != 0:
            Graph.addEdge(1,i)

Graph.printMatrix()