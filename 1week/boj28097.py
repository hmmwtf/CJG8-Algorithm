N = int(input())

arr = list(map(int, input().split()))

total = 0

for i in range(len(arr)):
    total += arr[i]
total += 8 * (N-1)

print((total // 24), total - (total // 24) * 24)