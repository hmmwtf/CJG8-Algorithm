import sys, bisect
input = sys.stdin.readline

# 사냥꾼의 수 = m, 동물의 수 = n, 사정거리 = l
m, n, l = map(int, input().split())
# 사대(총 쏘는 곳)
guns = list(map(int, input().split()))
guns.sort()

cnt = 0
for _ in range(n):
    x, y = map(int, input().split())
    # x축 기준으로 동물의 좌표랑 가까운 사냥꾼을 찾음
    idx = bisect.bisect_left(guns, x)
    
    flag = False
    #오른쪽
    if idx < len(guns):
        if abs(guns[idx] - x) + y <= l:
            flag = True
    # 왼쪽
    if idx > 0:
        if abs(guns[idx - 1] - x) + y <= l:
            flag = True
            
    if flag:
        cnt += 1

print(cnt)