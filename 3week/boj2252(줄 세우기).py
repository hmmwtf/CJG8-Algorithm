import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())
indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    indegree[b] += 1

def topologySort():
    result = []
    q = deque()
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        node = q.popleft()
        result.append(node)
        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                
    for i in result:
        print(i, end=' ')
    
topologySort()