import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n, m = map(int, input().strip().split())
    dp = [[0] * (n + 1) for i in range(m+1)]
    
    for i in range(0, m+1):
        dp[i][0] = 1
        if i <= n:
            dp[i][i] = 1
            
    for i in range(1, m+1):
        for j in range(1, min(i, n) + 1):
            if j == i:
                continue
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
    print(dp[m][n])