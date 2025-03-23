import sys

input = sys.stdin.readline

def bs(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

n = int(input().strip())
a = list(map(int, input().strip().split()))
m = int(input().strip())
b = list(map(int, input().strip().split()))

a.sort()
# 이진 탐색은 정렬이 되어있다는 가정하에 탐색을 진행
for bval in b:
    if bs(a, bval):
        print(1)
    else:
        print(0)