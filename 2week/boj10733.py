import sys

input = sys.stdin.readline

k = int(input().strip())

arr = []

for i in range(k):
    val = int(input().strip())
    if val == 0:
        arr.pop()
    else:
        arr.append(val)

print(sum(arr))