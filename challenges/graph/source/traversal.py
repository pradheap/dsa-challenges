from collections import deque

def recursive_dfs(graph, start):
    def dfs_helper(graph, start, path):
        path.append(start)
        for neighbor in graph.get_neighbors(start):
            if neighbor not in path:
                dfs_helper(graph, neighbor, path)
        return path
        
    return dfs_helper(graph, start, [])

def iterative_dfs(graph, start):
    vertices = [start]
    path = []
    while len(vertices) > 0:
        start = vertices.pop()
        path.append(start)
        for neighbor in graph.get_neighbors(start):
            if neighbor not in path:
                vertices.append(neighbor)
    
    return path

def iterative_bfs(graph, start):
    vertices = deque([start])
    path = []
    while len(vertices) > 0:
        start = vertices.popleft()
        path.append(start)
        for neighbor in graph.get_neighbors(start):
            if neighbor not in path:
                vertices.append(neighbor)
    
    return path