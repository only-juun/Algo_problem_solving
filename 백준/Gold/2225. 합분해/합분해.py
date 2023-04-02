# boj 2225. 합분해
MOD = 1000000000
n, k = tuple(map(int, input().split()))

# dp[i][j] := 지금까지 i개의 정수를 선택했고, 그 합이 j가 되는 경우의 수

dp = [[0] * (n + 1) for _ in range(k + 1)]

# 초기값 설정
for i in range(n + 1):
    dp[1][i] = 1

# dp 채우기
for i in range(1, k + 1):
    for j in range(n + 1):
        for x in range(0, j + 1):
            dp[i][j] = (dp[i][j] + dp[i - 1][x]) % MOD

print(dp[k][n])