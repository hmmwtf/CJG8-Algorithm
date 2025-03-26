import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())
cards = [int(input().strip()) for _ in range(n)]
heapq.heapify(cards)

total = 0
while  len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    twosum = a + b
    total += twosum
    heapq.heappush(cards, twosum)
    
print(total)