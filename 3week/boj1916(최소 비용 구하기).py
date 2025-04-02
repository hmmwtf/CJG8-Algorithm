import sys, heapq
input = sys.stdin.readline

def dijkstra(n, start, graph):

    INF = int(1e9)
    distances = [INF] * (n + 1)
    distances[start] = 0
    q = []
    
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distances[now]:
            continue
        
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    
    return distances

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    graph[a].append((b, c))
    
start, end = map(int, input().strip().split())

distances = dijkstra(n, start, graph)
print(distances[end])