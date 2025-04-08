import sys
input = sys.stdin.readline

# 행렬의 개수 입력 받기
n = int(input().strip())

# 행렬의 크기를 저장할 리스트 초기화
matrices = []

# 각 행렬의 행과 열 크기 입력 받기
for _ in range(n):
    r, c = map(int, input().strip().split())
    matrices.append((r, c))  # 행렬의 크기를 튜플로 저장

# DP 테이블 초기화: dp[i][j]는 i번째 행렬부터 j번째 행렬까지 곱할 때의 최소 연산 수를 저장
dp = [[0] * n for _ in range(n)]

# 부분 행렬의 길이를 2부터 n까지 증가시키며 최소 연산 수 계산
for length in range(2, n + 1):
    for start in range(n - length + 1):
        end = start + length - 1
        dp[start][end] = float('inf')  # 최소값을 찾기 위해 무한대로 초기화

        # start부터 end 사이의 모든 가능한 분할 지점 k에 대해 최소 연산 수 계산
        for k in range(start, end):
            # 행렬 곱셈 연산 수 계산
            cost = (dp[start][k] +  # A~B 부분의 최소 연산 수
                    dp[k + 1][end] +  # C~D 부분의 최소 연산 수
                    matrices[start][0] * matrices[k][1] * matrices[end][1])  # 두 부분을 합칠 때의 연산 수
            dp[start][end] = min(dp[start][end], cost)  # 최소 연산 수 갱신

# 전체 행렬을 곱할 때의 최소 연산 수 출력
print(dp[0][n - 1])