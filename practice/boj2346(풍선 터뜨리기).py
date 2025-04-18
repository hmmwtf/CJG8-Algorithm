import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
values = list(map(int, input().strip().split()))

q = deque((i+1, values[i]) for i in range(n))

result = []

while q:
    idx, step = q.popleft()
    result.append(idx)
    
    if step > 0:
        q.rotate(-(step-1))
    else:
        q.rotate(-step)
print(*result)