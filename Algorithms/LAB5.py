# LAB 5
from collections import deque

# def shortestPath(graph, start, end):
#     queue = deque([start])
#     visited = set()
    
#     while queue:
#         (node, path) = queue.popleft()
        
#         if node in visited:
#             continue
#         visited.add(node)
        
#         for neighbor in graph[node]:
#             if neighbor == end:
#                 return path + [end]
#             else:
#                 queue.append((neighbor, path + [neighbor]))
def shortestPath(graph, start, end):
    if start not in graph or end not in graph or graph == {}: # if start or end is not in the graph, or graph is empty
        return None
    queue = deque([start])
    visited = set()
    parent = {start: None}  # reconstruct the path later on
    while queue:
        current = queue.popleft()
        visited.add(current)
        
        if current == end: # If we are at the end, then backtrack to where we were, at the end we can just reverse it so we get the proper path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Reverse the path since we backtraced
        
        for neighbor in graph[current]: # if ew aare not at the end then check for the values of the key to see if where we can go and if it is visited or in the q
            if neighbor not in visited and neighbor not in queue:
                parent[neighbor] = current
                queue.append(neighbor)

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'F'],
    'E': ['B', 'F', 'G'],
    'F': ['C', 'E']
}

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# graph = {

# }

start = 'B'
end = 'F'
print(shortestPath(graph, start, end))
#AV