import sys
input = sys.stdin.readline

def count_tile(n):
    tile = [0] * (n + 3)
    tile[0] = 0
    tile[1] = 1
    tile[2] = 2
    
    for i in range(3, n+1):
        tile[i] = (tile[i-1] + tile[i-2]) % 10007
        
    return tile[n]
    
n = int(input().strip())
print(count_tile(n))