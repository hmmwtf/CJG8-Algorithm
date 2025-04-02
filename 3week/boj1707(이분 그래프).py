import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k = int(input().strip())

for _ in range(k):
    v, e = map(int, input().strip().split())
    graph = [[] for _ in range(v+1)]
    
    for _ in range(e):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        graph[b].append(a)
        
    colors = [0] * (v+1)
    def dfs(node, color):
        colors[node] = color
        for next in graph[node]:
            if colors[next] == 0:
                if not dfs(next, -color):
                    return False
            elif colors[next] == color:
                return False
        return True
    
    flag = True
    
    for i in range(1, v + 1):
        if colors[i] == 0:
            if not dfs(i, 1):
                flag = False
                break
    
    print("YES" if flag else "NO")