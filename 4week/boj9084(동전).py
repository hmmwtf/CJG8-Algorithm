import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    coins = list(map(int, input().strip().split()))
    money = int(input().strip())
    
    dp = [0] * (money + 1)
    dp[0] = 1
    
    for coin in coins:
        for x in range(coin, money + 1):
            dp[x] += dp[x-coin]
    
    print(dp[money])