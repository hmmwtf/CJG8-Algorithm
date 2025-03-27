import sys,heapq
input = sys.stdin.readline

n = int(input().strip())
q = []

for i in range(n):
    num = list(map(int, input().split()))
    if not q:
        for n in num:
            heapq.heappush(q, n)
    else:
        for n in num:
            if q[0] < n:
                heapq.heappush(q, n)
                heapq.heappop(q)

print(q[0])