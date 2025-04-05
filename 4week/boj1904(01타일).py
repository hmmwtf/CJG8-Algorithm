import sys
input = sys.stdin.readline

def binary(n):
    arr = [0] * (n+3)
    arr[0] = 0
    arr[1] = 1
    arr[2] = 2
    
    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]
        if arr[i] > 15746:
            arr[i] = arr[i] % 15746
    
    return arr[n] % 15746

n = int(input().strip())
print(binary(n))