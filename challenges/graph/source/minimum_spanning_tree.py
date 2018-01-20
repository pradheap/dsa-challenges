from lib.source.disjointset import DisjointSet

def minimum_spanning_tree(graph):
    djs = DisjointSet()
    # Add all vertices to the disjoint set.
    for v in graph.get_vertices():
        djs.make_set(v)
    
    min_cost = 0
    # edges are a list of tuples of the form (vertex1, vertex2, weight)
    edges = sorted(graph.get_edges(), key=lambda edge:edge[2])
    for edge in edges:
        # If vertex1 and vertex2 aren't in the same set, then union them.
        if djs.find_set(edge[0]) != djs.find_set(edge[1]):
            djs.merge_set(edge[0], edge[1])
            min_cost += edge[2]
    
    return min_cost