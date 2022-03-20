class Graph:

    def __init__(self):
        self.number_of_nodes =0
        self.adjacency_list = {}

    def insert_vertex(self,node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
            self.number_of_nodes += 1
            return

    def insert_edge(self,vertex1,vertex2):
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return
        print("edge already exists")

    def showConnections(self):
        for node in self.adjacency_list:
            print(f'{node} -->> {" ".join(map(str,self.adjacency_list[node]))}')


my_graph = Graph()

my_graph.insert_vertex(1)
my_graph.insert_vertex(2)
my_graph.insert_vertex(3)

my_graph.insert_edge(1,2)
my_graph.insert_edge(1,3)
my_graph.insert_edge(2,3)

my_graph.showConnections()


"""
1 -->> 2 3
2 -->> 1 3
3 -->> 1 2
"""

print(my_graph.adjacency_list)
#{1: [2, 3], 2: [1, 3], 3: [1, 2]}

print(my_graph.number_of_nodes)
#3
