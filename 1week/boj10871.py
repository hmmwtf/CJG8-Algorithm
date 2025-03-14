inputarr = input().split()
n, x = int(inputarr[0]), int(inputarr[1])

num = input().split()

for i in range(n):
    num[i] = int(num[i])

for i in range(n):
    if num[i] < x:
        print(num[i], end=" ")