n, m = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 0, max(trees)
result = 0

while left <= right:
    mid = (left + right) // 2
    total = 0
    for tree in trees:
        if tree > mid:
            total += (tree - mid) 

    if total >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)

"""
max_height = max(trees)
result = 0

for candidate in range(1, max_height+1):
    total = 0

    for tree in trees:
        diff = tree - candidate
        if diff > 0:
            total += diff
    
    if total >= m:
        result = candidate

print(result)
"""