class Edge:
    def __init__(self,node1,node2):
        self.node1 = node1
        self.node2 = node2

class Graph:
    def __init__(self,vertices = set(),edges = set()):
        self.vertices = vertices
        self.edges = edges
    def add_vertex(self,vertex):
        return self.vertices.add(vertex)
    def remove_vertex(self,vertex):
        if vertex in self.vertices:
            self.vertices.remove(vertex)
            self.edges = set([edge for edge in self.edges if edge.node1 != vertex and edge.node2 != vertex])
    def add_edge(self,edge):
        self.vertices.add(edge.node1)
        self.vertices.add(edge.node2)
        return self.edges.add(edge)
    def remove_edge(self,edge):
        return self.edges.remove(edge)
    def get_neighbors(self, vertex):
        neighbors = set()
        if vertex in self.vertices:
            for edge in self.edges:
                if edge.node1 == vertex:
                    neighbors.add(edge.node2)
                if edge.node2 == vertex:
                    neighbors.add(edge.node1)
        return neighbors
    def graph_to_dict(self):
        graphDict = {}
        for vertex in self.vertices:
            graphDict[vertex] = set()
        for edge in self.edges:
            graphDict[edge.node1].add(edge.node2)
            graphDict[edge.node2].add(edge.node1)
        return graphDict
    def bfs(self,s):
        Q = [s] #Initialize a queue
        visited = set([s]) #visited set keeps track of which nodes have been seen
        parent = {s:None}
        level = {s:0}
        while Q != []:
            u = Q.pop(0) #dequeue node u
            for v in self.get_neighbors(u): # explore all neighbor nodes v of node u
                if v not in visited: #only consider neighbors that haven't been seen yet
                    Q.append(v)
                    visited.add(v)
                    parent[v] = u
                    level[v] = level[u]+1
        return level
    def dfs(self,s):
        S = [s] #Initialize a stack
        visited = set([s]) #visited set keeps track of which nodes have been seen
        parent = {s:None}
        level = {s:0}
        while S != []:
            u = S.pop() #pop next node u from stack
            for v in self.get_neighbors(u):
                if v not in visited:
                    S.append(v)
                    visited.add(v)
                    parent[v] = u
                    level[v] = level[u]+1
        return level      

def dijkstra(graph):
    pass #TODO
def bellman_ford(graph):
    pass #TODO
