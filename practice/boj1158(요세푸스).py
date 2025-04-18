"""
import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
arr = list(range(1, n + 1))
result = []
idx = 0

while arr:
    idx = (idx + k - 1) % len(arr)
    result.append(arr.pop(idx))
    
print("<" + ", ".join(map(str, result)) + ">")
"""

import sys
from collections import deque

input = sys.stdin.readline

def josepose(n, k):
    q = deque(range(1, n+1))
    result = []
    
    while q:
        q.rotate(-(k-1))