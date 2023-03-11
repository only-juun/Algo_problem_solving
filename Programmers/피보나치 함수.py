# 문제: fibo(n)에서 fibo(0)과 fibo(1)의 실행 개수 구하기
# 입력 : 첫째 줄 - 테스트 케이스의 개수 T
#       각 테스트 케이스 별 N(0<=N<=40)

t = int(input())
arr = [int(input()) for _ in range(t)]

n = max(arr)

# dp 테이블
dp0 = [0 for _ in range(n + 1)]
dp1 = [0 for _ in range(n + 1)]

# 초기조건
dp0[0] = 1
dp0[1] = 0
dp1[0] = 0
dp1[1] = 1

# dp 테이블 채우기
for i in range(2, n+1):
    dp0[i] = dp0[i - 1] + dp0[i - 2]
    dp1[i] = dp1[i - 1] + dp1[i - 2]

# 출력: 연산을 사용하는 횟수의 최솟값을 출력
for a in arr:
    print(dp0[a], dp1[a])
