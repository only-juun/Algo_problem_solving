# 문제: 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수
# 입력 : 첫째 줄 - 집의 수 N(2 <= N <= 1000)
n = int(input())

# dp 테이블 & 초기조건
dp = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 초기조건

# dp 테이블 채우기
for i in range(1, n):
    dp[i][0] += min(dp[i-1][1],dp[i-1][2])
    dp[i][1] += min(dp[i-1][0],dp[i-1][2])
    dp[i][2] += min(dp[i-1][0],dp[i-1][1])

# 출력: 모든 집을 칠하는 비용의 최솟값
print(min(dp[n - 1]))
