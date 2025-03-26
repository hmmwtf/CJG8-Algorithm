import sys,heapq
input = sys.stdin.readline

n = int(input().strip())
q = []

for i in range(n):
    num = list(map(int, input().split()))
    for j in num:
        heapq.heappush(q, -j)
for i in range(n - 1):
    heapq.heappop(q)
print(-q[0])