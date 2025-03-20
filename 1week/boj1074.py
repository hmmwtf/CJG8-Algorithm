def z(n , r, c):
    if n == 0:
        return 0
    mid = 2 ** (n - 1)
    if  r < mid and c < mid:
        quad = 0
    elif r < mid and c >= mid:
        quad = 1
        c = c - mid
    elif r >= mid and c < mid:
        quad = 2
        r = r - mid
    elif r >= mid and c >= mid:
        quad = 3
        c = c - mid
        r = r - mid
    return quad * 4 **(n-1) + z(n-1, r, c) 

N, r, c = map(int, input().split())
print(z(N, r, c))