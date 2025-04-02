import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e = map(int, input().strip().split())
parent = [0] * (v + 1)
edges = []
ans = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, c = map(int, input().strip().split())
    edges.append((c, a, b))
    
edges.sort()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x] 

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans += c
        
print(ans)