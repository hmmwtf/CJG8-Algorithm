import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [float('inf')] * (n + 1)
dp[0] = 0

squares = []
i = 1
while i * i <= n:
    squares.append(i*i)
    i += 1
    
for x in range(1, n + 1):
    for square in squares:
        if square > x:
            break
        dp[x] = min(dp[x], dp[x - square] + 1)

print(dp[n])