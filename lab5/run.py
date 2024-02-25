from collections import deque

class Graph:
    def __init__(self):
        self.a = []  
        self.label = []  
        self.n = 0 
    def readAdjacencyMatrixFromFile(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.label = lines[0].split()[1:] 
            self.n = len(self.label)
            for line in lines[1:]:
                row = line.split()[1:]
                row = [int(x) for x in row] 
                self.a.append(row)    
    def setLabel(self, c):
        self.label = c    
    def breadthFirstTraverse(self, start):
        visited = [False] * self.n
        queue = deque()      
        visited[start] = True
        queue.append(start)
        while queue:
            start = queue.popleft()
            print(self.label[start], end=" ")
            for i in range(self.n):
                if self.a[start][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
    def depthFirstTraverse(self, start, visited):
        visited[start] = True
        print(self.label[start], end=" ")
        for i in range(self.n):
            if self.a[start][i] == 1 and not visited[i]:
                self.depthFirstTraverse(i, visited)


if __name__ == "__main__":
    g = Graph()
    g.readAdjacencyMatrixFromFile("adjacency_matrix.txt")
    g.setLabel(["A", "B", "C", "D", "E", "F"])

    print("Breadth First Traversal:")
    g.breadthFirstTraverse(0)
    print("\nDepth First Traversal:")
    visited = [False] * g.n
    g.depthFirstTraverse(0, visited)
