import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

dp = [[0] * (m + 1) for _ in range(n+1)]

for i in range(0, n + 1):
    dp[i][0] = 1
    if i <= m:
        dp[i][0] = 1
        
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
print(dp[n][m])