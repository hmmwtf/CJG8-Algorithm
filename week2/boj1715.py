import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())
left = []
right = []

for _ in range(n):
    x = int(input().strip())
    
    heapq.heappush(left, -x)
    
    c