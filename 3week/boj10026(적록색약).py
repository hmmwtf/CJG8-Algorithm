import sys
input = sys.stdin.readline

n = int(input().strip())
graph = [list(map(str, input().strip())) for _ in range(n)]
visited =[[0] * (n) for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def DFS(x, y, color):
    stack = [(x, y)]
    visited[x][y]  = 1
    
    while stack:
        cx, cy = stack.pop()
        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == color:
                    visited[nx][ny] = 1
                    stack.append((nx, ny))

# 정상인 경우               
normal = 0

# Flood Fill 
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            DFS(i, j, graph[i][j])
            normal += 1

# 적녹 색약          
daltonism = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

# 방문 배열 초기화
visited =[[0] * (n) for _ in range(n)]           

# Flood Fill 
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            DFS(i, j, graph[i][j])
            daltonism += 1
            
print(normal, daltonism)