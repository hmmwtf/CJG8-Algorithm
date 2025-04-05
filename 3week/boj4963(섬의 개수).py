import sys
input = sys.stdin.readline

direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def DFS(x, y):
    stack = [(x, y)]
    visited[x][y] = 1
    
    while stack:
        cx, cy = stack.pop()
        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = 1
                    stack.append((nx, ny))


while True:
    w, h = map(int, input().strip().split())
    if w == 0 and h == 0:
        break
    
    board = [list(map(int, input().strip().split())) for _ in range(h)]
    visited = [[0] * (w) for _ in range(h)]
    
    cnt = 0 
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and not visited[i][j]:
                DFS(i, j)
                cnt += 1
    print(cnt)