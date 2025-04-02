import sys
input = sys.stdin.readline

n = int(input().strip())
graph =[list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def DFS(x, y):
    stack = [(x,y)]
    visited[x][y] = 1
    cnt = 1
    
    while stack:
        cx, cy = stack.pop()
        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    stack.append((nx, ny))
                    cnt += 1
    return cnt

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            result.append(DFS(i, j))
            
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])