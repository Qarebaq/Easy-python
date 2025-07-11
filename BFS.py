from collections import deque

def bfs(graph, start):
    visited = set()           
    queue = deque()            
    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node) 
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')
