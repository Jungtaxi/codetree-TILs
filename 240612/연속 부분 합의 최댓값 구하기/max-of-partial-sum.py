import sys
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))

# init
dp = [-sys.maxsize for _ in range(n)]
dp[0] = graph[0]

# i번째까지의 연속된 합과 새롭게 만들어지는 수열을 비교하여 더 나은걸 채택
for i in range(1, n):
    dp[i] = max(dp[i-1] + graph[i], graph[i])

print(max(dp))