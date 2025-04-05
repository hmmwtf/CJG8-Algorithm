import sys
input = sys.stdin.readline

n = int(input().strip())
stair_cost = [0]

for _ in range(n):
    stair_cost.append(int(input().strip()))
    
dp = [0] * (n + 1)

dp[1] = stair_cost[1]

if n >= 2:
    dp[2] = stair_cost[1] + stair_cost[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-2] + stair_cost[i], dp[i-3] + stair_cost[i-1] + stair_cost[i])
        
print(dp[n])