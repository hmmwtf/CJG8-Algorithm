import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())
heap = []  

for i in range(n):
    x = int(input().strip())
    if x > 0:
        heapq.heappush(heap, -x)
    elif x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
