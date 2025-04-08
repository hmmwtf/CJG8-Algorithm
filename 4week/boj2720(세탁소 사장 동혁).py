import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    c = int(input().strip())
    q = c // 25
    d = (c - (q * 25)) // 10
    n = (c - (q * 25) - (d * 10)) // 5
    p = c % 5
    print(q,d,n,p, end = " ")