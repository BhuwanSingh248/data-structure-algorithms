
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = [None] * self.V
    
    def add_edge(self, src, dest):
        # adding a node to source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        #adding the source node to destination 
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node


    def __str__(self):
        for i in range(self.V):
            print("Adjacency list of vertex %i \n %i" %(i,i), end = "")
            temp:AdjNode = self.graph[i]
            while temp:
                print("-> %s" % temp.vertex, end = "")
                temp = temp.next
            print(" \n")
        return ""

if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    print(graph)