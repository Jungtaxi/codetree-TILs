# dp[6] = dp[4] + dp[3]
import sys
input = sys.stdin.readline
n = int(input())

dp = [1] *5
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = dp[1] + dp[2]

if n > 4:
    for i in range(5, n+1):
        dp[i] = dp[i-2] + dp[i-3]

print(dp[n])