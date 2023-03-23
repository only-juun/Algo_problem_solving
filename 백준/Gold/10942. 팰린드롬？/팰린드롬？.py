# boj 10942. 팰린드롬?

# 자연수 n개, 질문 m번
# 각 질문은 s, e: s번째부터 e번째 까지 팰린드롬인지(거꾸로=제대로)
# 대답은 1(yes) or 0(no)

# dp[i][j] := i부터 j까지의 숫자가 회문인지(0 or 1)
# 아이디어: 새로 추가되는 부분과 첫번째를 비교하고, 나머지 가운데 부분이 회문인지 판단
# 0~n까지 가면 배열 채우는 것이 불가능
# 반대로 n~0까지 거꾸로 가면 배열 채우기 가능

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
questions = [tuple(map(int, input().split())) for _ in range(m)]

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1

for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if (j - i) == 1:
            dp[i][j] = 1 if nums[i] == nums[j] else 0
        else:
            dp[i][j] = 1 if nums[i] == nums[j] and dp[i + 1][j - 1] else 0

for s, e in questions:
    print(dp[s - 1][e - 1])