import sys
input = sys.stdin.readline

t = int(input().strip())

def dfs(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if board[cx][cy] == 1:
            board[cx][cy] = 0  
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 1:
                    stack.append((nx, ny))
                    
for _ in range(t):
    m, n, k = map(int, input().strip().split())
    board = [[0] * n for _ in range(m)]
    
    for _ in range(k):
        x, y = map(int, input().strip().split())
        board[x][y] = 1
    
    cnt = 0
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)