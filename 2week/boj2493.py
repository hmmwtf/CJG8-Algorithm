import sys

input = sys.stdin.readline

n = int(input().strip())
heights = list(map(int, input().strip().split()))

result = [0] * n
stack = []

for i in range(n):
    height = heights[i]
    # 스택이 비어있지 않고, 현재 탑이 스택의 최상단 탑보다 높을 경우
    while stack and stack[-1][0] < height:
        stack.pop()
    # 스택이 비어있지 않다면, 스택의 최상단 탑이 현재 탑의 신호를 수신
    if stack:
        result[i] = stack[-1][1] + 1
    # 현재 탑을 스택의 추가(height, idx)
    stack.append((height, i))

print(' '.join(map(str, result)))