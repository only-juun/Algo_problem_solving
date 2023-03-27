n = int(input())
wine = [int(input()) for _ in range(n)]

# dp[i][j] := i번째에서 현재 j개 연속으로 선택했을 때 최대 포도주양

dp = [[0] * 3 for _ in range(n)]

dp[0][0] = 0
dp[0][1] = wine[0]
dp[0][2] = -1

for i in range(1, n):
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = dp[i - 1][0] + wine[i]
    dp[i][2] = dp[i - 1][1] + wine[i]

print(max(dp[n - 1]))