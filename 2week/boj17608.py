import sys

input = sys.stdin.readline

### 배열 순회 

n = int(input().strip())

height = []

for i in range(n):
    height.append(int(input().strip()))

cnt = 1
for i in range(len(height)-1, -1, -1):
    if height[i] > height.pop():
        cnt += 1
        view = height[i]

print(cnt)

### 스택

n = int(input().strip())
height = [int(input().strip()) for _ in range(n)]

stack = []

stack.append(height[-1])

for i in range(n - 2, -1, -1):
    if height[i] > stack[-1]:
        stack.append(height[i])

print(len(stack))