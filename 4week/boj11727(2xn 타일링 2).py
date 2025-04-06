import sys
input = sys.stdin.readline

def tile_cnt(n):
    tile = [0] * (n + 3)
    
    tile[0] = 0
    tile[1] = 1
    tile[2] = 3
    
    for i in range(3, n+1):
        tile[i] = (tile[i-1] + 2 * tile[i-2]) % 10007
    
    return tile[n]

n = int(input().strip())
print(tile_cnt(n))