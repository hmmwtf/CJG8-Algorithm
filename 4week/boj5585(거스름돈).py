import sys
input = sys.stdin.readline

pay = int(input().strip())

smalls = [500, 100, 50, 10, 5, 1]

change = 1000 - pay
cnt = 0

for coin in smalls:
    cnt += change // coin
    change %= coin

print(cnt)