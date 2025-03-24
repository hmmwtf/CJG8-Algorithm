import sys

input = sys.stdin.readline

zero_cnt = 0
one_cnt = 0

n = int(input().strip())
paper = []

for _ in range(n):
    paper.append(list(map(int, input().strip().split())))
    
def dc(x, y, size):
    global zero_cnt, one_cnt
    
    initial = paper[x][y]
    same = True
    
    for i in range(x, x + size):
        for j in range(y, y +size):
            if paper[i][j] != initial:
                same = False
                break
        if not same:
            break
    
    if same:
        if initial == 0:
            zero_cnt += 1
        else:
            one_cnt += 1
        return
    else:
        half = size // 2
        dc(x, y, half)
        dc(x, y+half, half)
        dc(x+half, y, half)
        dc(x+half, y+half, half)

dc(0, 0, n)

print(zero_cnt)
print(one_cnt)