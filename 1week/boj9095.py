import sys

input = sys.stdin.readline

def find(n):
    arr = []
    arr.append(1)
    arr.append(2)
    arr.append(4)

    if n <= 2:
        return n
    elif n == 3:
        return 4
    else:
        for i in range(0, n-2):
            val = arr[i+2] + arr[i+1] +arr[i]
            arr.append(val)
        return arr[n-1]

t = int(input())
for i in range(t):
    n = int(input())
    print(find(n))