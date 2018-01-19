

class UnweightedGraph():
    def __init__(self, is_directed=False):
        self._graph = {}
        self._is_directed = is_directed
    
    def is_directed(self):
        return self._is_directed
    
    def add_vertex(self, v):
        if v not in self._graph:
            self._graph[v] = []
    
    def add_edge(self, from_v, to_v):
        self.add_vertex(from_v)
        self.add_vertex(to_v)
        self._graph[from_v].append(to_v)
        if not self._is_directed:
            self._graph[to_v].append(from_v)
    
    def get_vertex(self, v):
        return self._graph[v]
    
    def get_vertices(self):
        return list(self._graph.keys())

    def get_edges(self):
        result = []
        for vertex in self._graph:
            for neighbor in self._graph[vertex]:
                if not self._is_directed and (neighbor, vertex) not in result:
                    result.append((vertex, neighbor))
                else:
                    result.append((vertex, neighbor))

        return result

    def get_neighbors(self, v):
        return self._graph[v]
            

class Vertex():
    def __init__(self, key):
        self.id = key
        self.neighbors = {}
    
    def add_neighbor(self, vertex, weight=0):
        self.neighbors[vertex] = weight
    
    def remove_neighbor(self, vertex):
        del self.neighbors[vertex]
    
    def get_neighbors(self):
        return  list(self.neighbors.keys())

    def get_weight(self, to_v):
        if to_v in self.get_neighbors():
            return self.neighbors[to_v]
        return None

    def get_key(self):
        return self.id

    def get_edges(self):
        edges = []
        for neighbor, weight in self.neighbors.items():
            edges.append((self.get_key(), neighbor, weight))
        return edges
        

class WeightedGraph():
    def __init__(self, is_directed=False):
        self._graph = {}
        self._is_directed = is_directed

    def is_directed(self):
        return self._is_directed

    def add_vertex(self, v):
        if v not in self._graph:
            self._graph[v] = Vertex(v)
    
    def add_edge(self, from_v, to_v, weight=0):
        self.add_vertex(from_v)
        self.add_vertex(to_v)
        self._graph[from_v].add_neighbor(to_v, weight)
        if not self._is_directed:
            self._graph[to_v].add_neighbor(from_v, weight)
        
    def get_vertices(self):
        return list(self._graph.keys())

    def get_vertex(self, v):
        if v in self._graph:
            return self._graph[v]
    
    def get_weight(self, from_v, to_v):
        return self._graph[from_v].get_weight(to_v)

    def get_neighbors(self, v):
        return self.get_vertex(v).get_neighbors()
    
    def get_edges(self):
        edges = []
        for v in self._graph.values():
            edges.extend(v.get_edges())
        return edges