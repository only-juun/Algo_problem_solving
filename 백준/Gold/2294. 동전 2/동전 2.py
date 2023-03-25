import sys
INF = sys.maxsize
n, k = tuple(map(int, input().split()))
coins = [int(input()) for _ in range(n)]

dp = [INF] * (k + 1)
dp[0] = 0
for coin in coins:
    for i in range(k - coin + 1):
        dp[i + coin] = min(dp[i] + 1, dp[i + coin])

print(dp[k] if dp[k] != INF else -1)