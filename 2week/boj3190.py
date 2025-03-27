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


import sys
from collections import deque

input = sys.stdin.readline

# 보드 크기와 사과의 개수 입력
n = int(input().strip())
k = int(input().strip())
apples = set()

# 사과 위치를 0-indexed 튜플로 저장
for _ in range(k):
    x, y = map(int, input().strip().split())
    apples.add((x-1, y-1))

# 방향 전환 횟수와 정보를 입력받아 저장 (시간, 방향)
l = int(input().strip())
directions = []
for _ in range(l):
    x, c = input().strip().split()
    directions.append((int(x), c))
    
# 이동 방향을 오른쪽, 아래, 왼쪽, 위 순서로 정의
# 여기서 board에서 행(i)와 열(j)를 사용하므로:
# 오른쪽: (행 변화 0, 열 변화 +1)
# 아래: (행 변화 +1, 열 변화 0)
# 왼쪽: (행 변화 0, 열 변화 -1)
# 위: (행 변화 -1, 열 변화 0)
dx = [0, 1, 0, -1]  # 행의 변화량
dy = [1, 0, -1, 0]  # 열의 변화량
current_direction = 0  # 초기 방향: 오른쪽

time = 0  # 경과 시간
snake = deque()  # 뱀의 몸통을 저장할 deque (머리: 오른쪽, 꼬리: 왼쪽)
snake.append((0, 0))  # 시작점 (0,0)

dir_idx = 0  # 방향 전환 정보를 추적할 인덱스

while True:
    time += 1  # 1초 증가
    head_x, head_y = snake[-1]  # 현재 뱀의 머리 위치
    # 현재 방향으로 다음 위치 계산
    nx = head_x + dx[current_direction]
    ny = head_y + dy[current_direction]
    
    # 벽에 부딪혔는지 확인 (보드 범위 벗어남)
    if not (0 <= nx < n and 0 <= ny < n):
        break
    
    # 자기 자신(몸통)에 부딪혔는지 확인
    if (nx, ny) in snake:
        break
    
    # 새로운 머리 위치 추가
    snake.append((nx, ny))
    
    # 이동한 위치에 사과가 있다면 사과 제거(꼬리 유지 → 몸 길이 증가)
    if (nx, ny) in apples:
        apples.remove((nx, ny))
    else:
        # 사과가 없으면 꼬리 제거하여 몸 길이 유지
        snake.popleft()
    
    # 지정된 시간에 도달하면 방향 전환 처리
    if dir_idx < len(directions) and time == directions[dir_idx][0]:
        turn = directions[dir_idx][1]
        if turn == "L":
            current_direction = (current_direction - 1) % 4  # 왼쪽 회전
        elif turn == "D":
            current_direction = (current_direction + 1) % 4  # 오른쪽 회전
        dir_idx += 1

# 게임 종료 후 경과 시간 출력
print(time)
