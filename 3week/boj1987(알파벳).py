import sys
input = sys.stdin.readline

r, c = map(int, input().strip().split())
board = [list(input().strip()) for _ in range(r)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, visited, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            next_char = board[nx][ny]
            next_bit = 1 << (ord(next_char) - ord('A'))
            if not (visited & next_bit):
                dfs(nx, ny, visited | next_bit, cnt + 1)

max_cnt = 0
initial_bit = 1 << (ord(board[0][0]) - ord('A'))
dfs(0, 0, initial_bit, 1)
print(max_cnt)