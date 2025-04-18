import sys, heapq

input = sys.stdin.readline

n = int(input().strip())
heap = []

for _ in range(n):
    for num in map(int, input().split()):
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heapreplace(heap, num)

print(heap[0])