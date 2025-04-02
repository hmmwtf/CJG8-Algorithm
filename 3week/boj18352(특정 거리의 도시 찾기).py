import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    
q = deque([x])
visited = [-1 for _ in range(n+1)]
visited[x] = 0

def bfs():
    while q:
        x = q.popleft()
        for node in graph[x]:
            if visited[node] == -1:
                visited[node] = visited[x] + 1
                q.append(node)

bfs()
if visited.count(k) == 0:
    print(-1)
else:
    for i in range(n+1):
        if visited[i] == k:
            print(i)