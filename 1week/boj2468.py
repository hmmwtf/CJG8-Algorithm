import sys

input = sys.stdin.readline

def DFS(i, j, water_level, location, visited):
    n = len(location)
    visited[i][j] = True
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n:
            if not visited[ni][nj] and location[ni][nj] > water_level:
                DFS(ni, nj, water_level, location, visited)

n = int(input().strip())
location = []

for i in range(n):
    row = list(map(int, input().split()))
    location.append(row)

min_height = min(min(row) for row in location)
max_height = max(max(row) for row in location)

max_safe_area = 0
for water_level in range(0, max_height+1):
    visited = [[False] * n for _ in range(n)]
    safe_area_count = 0
    for i in range(n):
        for j in range(n):
            if location[i][j] > water_level and not visited[i][j]:
                DFS(i, j, water_level, location, visited)
                safe_area_count += 1
    max_safe_area = max(max_safe_area, safe_area_count)