# 문제: n 킬로그램 배달 - 최대한 적은 봉지(3 or 5의 조합)
# 입력: 첫째 줄에 N(3 ≤ N ≤ 5000)
n = int(input())

# dp 테이블 정의
dp = [0 for _ in range(n + 3)]

# 출력: 봉지의 최소 개수, N킬로그램을 만들 수 없다면 -1
# 초기조건
dp[0] = 0
dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 0
dp[5] = 1

# dp 테이블 채우기

if n >= 5:
    for i in range(6, n + 1):
        if dp[i - 3] == 0 and dp[i - 5] == 0:
            dp[i] = 0
        elif dp[i - 3] == 0:
            dp[i] = dp[i - 5] + 1
        elif dp[i - 5] == 0:
            dp[i] = dp[i - 3] + 1
        else:
            dp[i] = min(dp[i - 3], dp[i - 5]) + 1

print(dp[n] if dp[n] > 0 else -1)