import sys
from collections import deque
input = sys.stdin.readline
"""
n,k = map(int, input().strip().split())
arr = [i for i in range(1, n+1)]
q = []

idx = 0

while len(arr) > 0:
    idx = (idx + k -1) % len(arr)
    q.append(arr.pop(idx))

print('<' + ",".join(map(str, q))  + '>')
"""

def jp(n, k):
    queue = deque(range(1, n+1))
    result = []
    
    while queue:
        queue.rotate(-(k-1))
        result.append(queue.popleft())
        
    return result

n,k = map(int, input().strip().split())
output = jp(n, k)
print("<" + ", ".join(map(str, output)) + ">")