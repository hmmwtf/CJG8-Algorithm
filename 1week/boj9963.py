def dfs(n):
    global ans
    if n == N:
        ans += 1
        return 

    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j]:
            v1[j] = v2[n+j] = v3[n-j] = 1
            dfs(n+1)
            v1[j] = v2[n+j] = v3[n-j] = 0

N = int(input())

ans = 0
v1 = [0] *N
v2 = [0] * (2 * N)
v3 = [0] * (2 * N)
dfs(0)
print(ans) 




n = int(input())

pos = [0] * n
flag_a = [False] * n            # 각 열에 퀸을 배치했는지 체크
flag_b = [False] * (2 * n - 1)  # 각 대각선(↙↗)에 퀸을 배치했는지 체크
flag_c = [False] * (2 * n - 1)  # 각 대각선(↖↘)에 퀸을 배치했는지 체크

count = 0  

def set(i: int) -> None:
    global count
    for j in range(n):
        if not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + n - 1]:
            pos[i] = j
            if i == n - 1:
                count += 1
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + n - 1] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + n - 1] = False

set(0)
print(count)

"""
n = int(input())

queen = [-1] * n

def is_able_attack(row, col):
    for i in range(row):
        if queen[i] == col:
            return False
        if abs(row - i) == abs(col- queen[i]):
            return False
    return True

def recursion(n, row):
    count = 0
    # 탈출 조건
    if row == n:
        return 1

    for col in range(n):
        # 퀸이 공격 가능한지 검사 반환값 == bool
        # 만약 공격 가능하다 판단되면 pass
        # 공격 불가인 경우 재귀 함수로 다음 퀸 배치
        if is_able_attack(row, col):
            queen[row] = col
            count += recursion(n, row+1)
    return count

print(recursion(n, 0))

"""

n = int(input())

queens = [-1] * n

def is_able_attack(row, col):
    for i in range(row):
        if queens[i] == col:
            return False
        if abs(row - i) == abs(col - queens[i]):
            return False
    return True

def recursion(n, row):
    cnt = 0
    if row == n:
        return 1
    
    for col in range(n):
        if is_able_attack(row, col):
            queens[row] = col
            count += recursion(n, row+1)
    return count

print(recursion(n, 0))


