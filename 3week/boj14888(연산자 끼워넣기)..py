import sys
from itertools import permutations
input = sys.stdin.readline

# 순열로 풀기
"""
n = int(input().strip())
num_list = list(map(int, input().strip().split()))
plus, minus, multi, divide = map(int, input().split())
operator = ['+' for _ in range(plus)] + ['-' for _ in range(minus)] + ['*' for _ in range(multi)] + ['/' for _ in range(divide)]
permu = list(set(permutations(operator, n-1)))

result = []

for part in permu:
    start = num_list[0]
    for j in range(0, n-1):
        if part[j] == '+':
            start += num_list[j+1]
        if part[j] == '-':
            start -= num_list[j+1]
        if part[j] == '*':
            start *= num_list[j+1]
        if part[j] == '/':
            if start < 0:
                start = -start
                start //= num_list[j+1]
                start = -start
            else:
                start //= num_list[j+1]
    result.append(start)

print(max(result))         
print(min(result))
"""

# DFS로 풀어보기
n = int(input().strip())
num = list(map(int, input().strip().split()))
add, sub, mul, div = map(int, input().strip().split())

mx = -int(1e9)
mn = int(1e9)

def dfs(add, sub, mul, div, sum, idx):
    global mx, mn
    if idx == n:
        mx = max(mx, sum)
        mn = min(mn, sum)
        return
    if add:
        dfs(add-1, sub, mul, div, sum + num[idx], idx + 1)
    if sub:
        dfs(add, sub-1, mul, div, sum - num[idx], idx + 1)
    if mul:
        dfs(add, sub, mul-1, div, sum * num[idx], idx + 1)
    if div:
        dfs(add, sub, mul, div-1, int(sum / num[idx]), idx + 1)

dfs(add, sub, mul, div, num[0], 1)
print(mx)
print(mn)