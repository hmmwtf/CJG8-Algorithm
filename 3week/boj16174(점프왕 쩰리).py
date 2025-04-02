import sys
input = sys.stdin.readline

n = int(input().strip())
board = [list(map(int, input().strip().split())) for _ in range(n)]
stack = [(0, 0)]
visited = set()
visited.add((0, 0))

while stack:
    x, y = stack.pop()
    if (x, y) == (n - 1, n - 1):
        print("HaruHaru")
        break
    jump = board[x][y]
    for dx, dy in [(jump, 0),(0, jump)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
            visited.add((nx, ny))
            stack.append((nx, ny))
else:
    print("Hing")