import itertools
n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

for r in range(1, n+1):
    for com in itertools.combinations(arr, r):
        if sum(com) == s:
            cnt += 1

print(cnt)