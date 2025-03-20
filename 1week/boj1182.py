from itertools import combinations
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for r in range(1, n+1):
    for part in combinations(arr, r):
        if sum(part) == s:
            cnt += 1

print(cnt)