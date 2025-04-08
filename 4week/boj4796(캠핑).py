import sys
input = sys.stdin.readline

c = 1
while True:
    l, p, v = map(int, input().strip().split())
    
    if l == 0 and p == 0 and v == 0:
        break
    
    cnt = (v // p) * l + min(v%p, l)
    print("Case {}: {}".format(c, cnt))
    c += 1