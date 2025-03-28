import sys, math
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n,m = map(int, input().strip().split())
    print(math.comb(m, n))
    