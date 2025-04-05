import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())  
graph = [list(input().strip()) for _ in range(m)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    q = deque()
    now = graph[x][y]
    q.append((x, y))
    graph[x][y] = "O"  
    cnt = 0
    while q:
        cx, cy = q.popleft()
        cnt += 1
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == now:
                q.append((nx, ny))
                graph[nx][ny] = "O"
    return cnt

w_cnt = 0
b_cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == "W":
            w_cnt += bfs(i, j) ** 2
        elif graph[i][j] == "B":
            b_cnt += bfs(i, j) ** 2

print(w_cnt)
print(b_cnt)
