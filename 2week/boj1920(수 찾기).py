

import sys

input = sys.stdin.readline

# set을 이용한 중복 제거 풀이 방법
"""
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

nodupA = set(a)

for x in b:
    if x in nodupA:
        print(1)
    else:
        print(0)
"""

# 이진 탐색(Binary Search)를 이용한 풀이 방법

def B_S(arr, target):
    left, right = 0, len(arr) -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))

for val in b:
    if B_S(a, val):
        print(1)
    else:
        print(0)
        