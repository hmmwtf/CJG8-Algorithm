import sys

input = sys.stdin.readline

def can_place(mid, house, c):
    # 첫 번째 집에 공유기 설치
    cnt = 1
    # 마지막으로 공유기를 설치한 집의 위치
    last = house[0]
    for i in range(1, len(house)):
        if house[i] - last >= mid:
            cnt += 1
            last = house[i]
    # 설치한 공유기의 개수가 필요한 공유기 개수(c) 이상이면 True
    return cnt >= c

n, c = map(int, input().strip().split())  

house = [int(input().strip()) for _ in range(n)]
house.sort()

# 거리 기준 이진 탐색
left, right = 1, house[-1] - house[0]
ans = 0

while left <= right:
    mid = (left + right) // 2
    if can_place(mid, house, c):  
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)