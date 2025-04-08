import sys
input = sys.stdin.readline

n = int(input().strip())
seats = list(map(str, input().strip()))

scnt = 0
lcnt = 0
for seat in seats:
    if seat == 'S':
        scnt += 1
    if seat == 'L':
        lcnt += 1
        
print(min(n, scnt + (lcnt // 2) + 1))