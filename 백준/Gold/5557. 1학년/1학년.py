n = int(input())
nums = list(map(int, input().split()))
target = nums[-1]

# dp[i][j] := i번째에서 j를 만들 수 있는 경우의 수
dp = [[0] * 21 for _ in range(n)]
dp[0][nums[0]] = 1

for i in range(1, n - 1):
    for j in range(21):
        if j + nums[i] <= 20:
            dp[i][j] += dp[i - 1][j + nums[i]]
        if j - nums[i] >= 0:
            dp[i][j] += dp[i - 1][j - nums[i]]
            
print(dp[n - 2][target])