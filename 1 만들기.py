# 문제: 연산1. 3으로 나누기 / 연산2. 2로 나누기 / 연산3. 1빼기
# 연산 세 개를 적절히 사용해서 1 만들기 
# 입력 : 정수 N
n = int(input())
# dp 테이블
dp = [0 for _ in range(n + 1)]

# 초기조건
dp[0] = 0
dp[1] = 0
# dp[2] = 1
# dp[3] = 1

# dp 테이블 채우기
for i in range(2, n+1):
    if i%3 == 0:
        if i%2 == 0:
            dp[i] = min(dp[i // 3], dp[i // 2], dp[i - 1]) + 1
        else:
            dp[i] = min(dp[i // 3], dp[i - 1]) + 1

    else:
        if i%2 == 0:
            dp[i] = min(dp[i // 2], dp[i - 1]) + 1
        else:
            dp[i] = dp[i - 1] + 1

# 출력: 연산을 사용하는 횟수의 최솟값을 출력
print(dp[n])