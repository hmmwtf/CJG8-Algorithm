import sys
input = sys.stdin.readline

a = 300
b = 60
c = 10

t = int(input().strip())
acnt = 0
bcnt = 0
ccnt = 0

if t >= 300:
    acnt += t // 300
    bcnt += (t - (300 * acnt)) // 60
    ccnt += (t - (300 * acnt) - (60 * bcnt)) // 10
else:
    bcnt += t // 60
    ccnt += (t - (60 * bcnt)) // 10

if t == (300 * acnt) + (60 *bcnt) + (10 * ccnt):
    print(acnt, bcnt, ccnt, end= " ")
else:
    print(-1)