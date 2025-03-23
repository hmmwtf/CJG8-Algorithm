import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())


left = []
right = []

for _ in range(n):
    x = int(input().strip())
    
    heapq.heappush(left, -x)
    
    if left and right and (-left[0] > right[0]):
        heapq.heappush(right, -heapq.heappop(left))
        
    if len(left) < len(right):
        heapq.heappush(left, -heapq.heappop(right))
    elif len(left) - len(right) > 1:
        heapq.heappush(right, -heapq.heappop(left))
        
    median = -left[0]
    print(median)