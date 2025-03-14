import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)

arr.sort()

for j in range(n):
    print(arr[j])