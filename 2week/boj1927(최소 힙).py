import sys, heapq

input = sys.stdin.readline

n = int(input().strip())
q = []

for i in range(n):
    order = int(input().strip())
    if order == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, order)
        