import sys
input = sys.stdin.readline

v = int(input().strip())
e = int(input().strip())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (v + 1)

cnt = 0

def dfs(node):
    global cnt
    visited[node] = True
    for next in graph[node]:
        if not visited[next]:
            cnt += 1
            dfs(next)
            
dfs(1)
print(cnt)