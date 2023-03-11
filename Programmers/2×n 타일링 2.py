# 문제: 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수
# 입력 : 첫째 줄 - N(1 <= N <= 1000)
n = int(input())

# dp 테이블
dp = [0 for _ in range(n + 1)]

# 초기조건
dp[0] = 1
dp[1] = 1

# dp 테이블 채우기
for i in range(2, n+1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007

# 출력: 연산을 사용하는 횟수의 최솟값을 출력
print(dp[n])