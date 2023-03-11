# 문제: 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 구하기
# 규칙
# 1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
# 2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 3. 마지막 도착 계단은 반드시 밟아야 한다.

# 입력 : 계단 수 N(1 <= N <= 300)
n = int(input())
steps = [0] + [int(input()) for _ in range(n)]

# dp 테이블
dp1 = [0 for _ in range(n + 1)]
dp2 = [0 for _ in range(n + 1)]

# 초기조건
dp1[0] = 0
dp1[1] = steps[1]
dp2[0] = 0
dp2[1] = 0

if n > 1:
    dp1[2] = steps[1] + steps[2]
    dp2[2] = steps[2]

# dp 테이블 채우기
for i in range(3, n + 1):
    dp1[i] = dp2[i-1] + steps[i]
    dp2[i] = max(dp1[i-2], dp2[i-2]) + steps[i]

# 출력: 계단 오르기 게임 최댓값
print(max(dp1[n],dp2[n]))