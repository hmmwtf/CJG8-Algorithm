import sys
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]
time = 0  # 경과 시간(년)
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 방향 벡터

# DFS 함수 정의
def DFS(x, y):
    stack = [(x, y)]
    visited[x][y] = 1  # 방문 표시 및 인접한 바다 칸 수를 세기 위한 초기값 설정
    
    while stack:
        cx, cy = stack.pop()
        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    # 인접한 칸이 바다인 경우, 현재 빙산 칸의 visited 값을 증가
                    visited[cx][cy] += 1
                elif graph[nx][ny] > 0 and visited[nx][ny] == 0:
                    # 인접한 칸이 빙산이고 아직 방문하지 않은 경우
                    visited[nx][ny] = 1
                    stack.append((nx, ny))

# 시뮬레이션 시작
while True:
    cnt = 0  # 현재 빙산 덩어리의 개수
    visited = [[0] * m for _ in range(n)]  # 방문 여부 및 인접한 바다 칸 수를 저장할 배열 초기화
    
    # 모든 칸을 순회하며 빙산 덩어리 수 세기
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and visited[i][j] == 0:
                DFS(i, j)
                cnt += 1
    
    if cnt >= 2:
        # 빙산 덩어리가 2개 이상으로 분리된 경우, 경과 시간을 출력하고 종료
        print(time)
        break
    if cnt == 0:
        # 모든 빙산이 녹아 없어진 경우, 0을 출력하고 종료
        print(0)
        break
    
    # 빙산 녹이기
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 0:
                # 현재 칸의 빙산 높이에서 (인접한 바다 칸 수)만큼 감소
                graph[i][j] -= (visited[i][j] - 1)
                if graph[i][j] < 0:
                    # 빙산 높이가 음수가 되지 않도록 0으로 설정
                    graph[i][j] = 0
                    
    time += 1  # 1년 경과