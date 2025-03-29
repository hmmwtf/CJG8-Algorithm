import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().strip().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n+1):
    graph[i].sort()

dfs_visited = [False] * (n+1)
dfs_result = []

def dfs(node):
    dfs_visited[node] = True
    dfs_result.append(node)
    for x in graph[node]:
        if not dfs_visited[x]:
            dfs(x)

bfs_visited = [False] * (n+1)
bfs_result = []

def bfs(start):
    q = deque([start])
    bfs_visited[start] = True
    while q:
        node = q.popleft()
        bfs_result.append(node)
        for near in graph[node]:
            if not bfs_visited[near]:
                bfs_visited[near] = True
                q.append(near)         

dfs(v)
print(" ".join(map(str, dfs_result)))
bfs(v)
print(" ".join(map(str, bfs_result)))