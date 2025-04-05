import sys
input = sys.stdin.readline

m, n, k = map(int, input().strip().split())
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().strip().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
            
def DFS(x, y):
    stack = [(x, y)]
    area_size = 0
    while stack:
        cx, cy = stack.pop()
        if graph[cx][cy] == 0:
            graph[cx][cy] = 1
            area_size += 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy+ dy
                if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                    stack.append((nx, ny))
                    
    return area_size

areas = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            areas.append(DFS(i, j))
            
areas.sort()
print(len(areas))
print(' '.join(map(str, areas)))






import sys
input = sys.stdin.readline

