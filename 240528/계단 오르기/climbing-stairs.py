# dp[6] = dp[4] + dp[3]
import sys
input = sys.stdin.readline
n = int(input())

dp = [1] * 4
dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 1

if n > 3:
    for i in range(4, n+1):
        dp.append(dp[i-2] + dp[i-3])

print(dp[n])