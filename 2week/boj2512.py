import sys

input = sys.stdin.readline

n = int(input().strip())
budgets = list(map(int, input().strip().split()))
total = int(input().strip())

# 처음 내가 푼 방식
"""
max_budget = 0
if sum(budgets) <= total:
    max_budget = max(budgets)
else:
    budgets.sort()
    current_budget = 0
    max_budget = 0
    for i in range(n):
        if current_budget + budgets[i] * (n - i) > total:
            max_budget = (total - current_budget) // (n - i)
            break
        current_budget += budgets[i]
        max_budget =budgets[i]
            
print(max_budget)
"""

#이진 탐색
low, high = 0, max(budgets)
result = 0

while low <= high:
    mid = (low + high) // 2
    s = sum(b if b < mid else mid for b in budgets)
    
    if s <= total:
        result = mid
        low = mid + 1
    else:
        high = mid - 1
        
print(result)