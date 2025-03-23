import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
k = int(input().strip())

apples = set()
for _ in range(k):
    r, c = map(int, input().split())
    apples.add((r-1, c-1))

l = int(input().strip())
turns = []
for _ in range(l):
    x, c = input().split()
    turns.append((int(x), c))

dr = [0, 1, 0, -1]  
dc = [1, 0, -1, 0]
current_dir = 0

time = 0
snake = deque([(0, 0)])
snake_set = {(0, 0)}

turn_idx = 0

while True:
    time += 1
    head_r, head_c = snake[0]
    nr = head_r + dr[current_dir]
    nc = head_c + dc[current_dir]

    if not (0 <= nr < n and 0 <= nc < n) or (nr, nc) in snake_set:
        break

    snake.appendleft((nr, nc))
    snake_set.add((nr, nc))

    if (nr, nc) in apples:
        apples.remove((nr, nc))
    else:
        tail = snake.pop()
        snake_set.remove(tail)

    if turn_idx < len(turns) and turns[turn_idx][0] == time:
        if turns[turn_idx][1] == 'L':
            current_dir = (current_dir - 1 + 4) % 4
        elif turns[turn_idx][1] == 'D':
            current_dir = (current_dir + 1) % 4
        turn_idx += 1

print(time)
