import sys
input = sys.stdin.readline

n = int(input().strip())
video = [list(map(int, list(input().strip()))) for _ in range(n)]

def quad_tree(x, y, n):
    fv = video[x][y]
    same = True
    for i in range(x, x+n):
        for j in range(y, y+n):
            if video[i][j] != fv:
                same = False
                break
        if not same:
            break
    
    if same:
        return str(fv)
    else:
        half = n // 2
        quad1 = quad_tree(x, y, half)
        quad2 = quad_tree(x, y+half, half)
        quad3 = quad_tree(x+half, y, half)
        quad4 = quad_tree(x+half, y+half, half)
        return "(" + quad1 + quad2 + quad3 + quad4 + ")"
print(quad_tree(0, 0, n))
