import sys
input = sys.stdin.readline

n = int(input().strip())

family = [[] for _ in range(n+1)]

f1, f2 = map(int, input().strip().split())
m = int(input().strip())

for i in range(m):
    a, b = map(int, input().strip().split())
    family[a].append(b)
    family[b].append(a)

def dfs(graph, start, target):
    stack = [(start, 0)]
    visited = set()
    
    while stack:
        node, degree = stack.pop()
        if node == target:
            return degree
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, degree + 1))
    
    return -1



import sys
input = sys.stdin.readline

n = int(input().strip())
graph = [[] for _ in range(n+1)]
n1, n2 = map(int, input().strip().split())
m = map(int, input().strip())

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    
def DFS(graph, start, target):
    stack = [(start, 0)]
    visited = set()
    
    while stack:
        node, degree = stack.pop()
        if node == target:
            return degree
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, degree + 1))
                    
    return -1
