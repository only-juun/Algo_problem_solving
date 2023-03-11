# 문제: 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수
# 입력 : 첫째 줄 - 테스트 케이스의 개수 T
#       각 테스트 케이스 별 정수 N(0 < N < 11)

t = int(input())
arr = [int(input()) for _ in range(t)]

n = max(arr)

if n == 1:
    print(1)

else:
    # dp 테이블
    dp = [0 for _ in range(n + 1)]

    # 초기조건
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    #dp[3] = 4

    # dp 테이블 채우기
    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    # 출력: 연산을 사용하는 횟수의 최솟값을 출력
    for a in arr:
        print(dp[a])
