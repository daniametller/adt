from collections import deque, defaultdict

def bfs(graph, start):
    nodes = deque()
    nodes.append(graph[start])
    visited = [start]
    while nodes:
        current_node = nodes.popleft()
        for node in current_node:
            if not node in visited:
                visited.append(node)
                nodes.append(graph[node])
        
    return visited

graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
print(bfs(graph, 'A'))
