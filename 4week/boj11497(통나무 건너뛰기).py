import sys
from collections import deque

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    l = list(map(int, input().strip().split()))
    l.sort(reverse= True)

    q = deque()
    q.append(l[0])
    for i in range(1, len(l)):
        if i % 2 == 1:
            q.appendleft(l[i])
        else:
            q.append(l[i])
    
    dist = [0] * n
    
    for i in range(0,len(l)-1):
        dist[i] = abs(q[i+1] - q[i])
    
    dist.append(abs(q[len(l) - 1] - q[0]))
    print(max(dist))