import sys, heapq
input = sys.stdin.readline
result = []

n = int(input().strip())
while True:
    x = int(input().strip())
    if x == -1:
        break
    elif x == 0:
        result.pop(0)
    else:
        if len(result) < n:
            result.append(x)

if len(result) == 0:
    print("empty")
else:
    print(" ".join(map(str, result)), end=" ")
    
    
# deque로 푸는 법
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
q = deque()

while True:
    x = int(input().strip())
    if x == -1:
        break
    elif x == 0:
        if q:
            q.popleft()
    else:
        if len(q) < n:
            q.append(x)

if not q:
    print("empty")
else:
    print(" ".join(map(str, q)))
