n = int(input())
arr = []

for i in range(n):
    num = int(input())
    arr.append(num)

arr.sort()

for j in range(n):
    print(arr[j])