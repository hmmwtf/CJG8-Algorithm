import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().strip())

graph = [[] for i in range(n+1)]
# graph = [[] for i in range(n+1)]와 [[] * (n+1)]의 차이:

for i in range(n-1):
    node1, node2 = map(int, input().strip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    
visited = [0] * (n+1)

def dfs(node):
    for x in graph[node]:
        if visited[x] == 0:
            visited[x] = node
            dfs(x)
            
dfs(1)

for i in range(2, n+1):
    print(visited[i])