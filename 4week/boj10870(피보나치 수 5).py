import sys
input = sys.stdin.readline

def fibo(n):
    arr = []
    arr.append(0)
    arr.append(1)
    
    for i in range(2, n+1):
        arr.append(arr[i-1] + arr[i-2])
    
    return arr[n]

n = int(input().strip())
print(fibo(n))