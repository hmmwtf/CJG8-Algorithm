import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    coins = list(map(int, input().strip().split()))
    money = int(input().strip())