class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            if v2 not in self.adj_list[v1] and v1 not in self.adj_list[v2]:
                self.adj_list[v1].append(v2)
                self.adj_list[v2].append(v1)
                return True
        return False
    
    def remove_edge(self, v1, v2):
        if v2 in self.adj_list[v1] and v1 in self.adj_list[v2]:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False
    
    def remove_vertex(self, v):
        if v in self.adj_list.keys():
            for vertex in self.adj_list[v]:
                self.adj_list[vertex].remove(v)
            del self.adj_list[v]
            return True
        return False
    

myGraph = Graph()
myGraph.add_vertex("A")
myGraph.add_vertex("B")
myGraph.add_vertex("C")
myGraph.add_vertex("D")
print("====== MY VERTICES ======")
myGraph.print_graph()
print("====== ADDING EDGE ======")
myGraph.add_edge("A","B")
myGraph.add_edge("A","C")
myGraph.add_edge("A","D")
myGraph.add_edge("B","D")
myGraph.add_edge("C","D")
myGraph.print_graph()
print("====== REMOVING VERTEX ======")
print(myGraph.remove_vertex("D"))
myGraph.print_graph()


# print("====== REMOVE EDGE ======")
# print(myGraph.remove_edge("A", "C"))
# myGraph.print_graph()