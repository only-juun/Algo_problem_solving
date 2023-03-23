# boj 10942. 팰린드롬?

# 자연수 n개, 질문 m번
# 각 질문은 s, e: s번째부터 e번째 까지 팰린드롬인지(거꾸로=제대로)
# 대답은 1(yes) or 0(no)

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
questions = [tuple(map(int, input().split())) for _ in range(m)]

dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i] = 1

for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if i == j:
            continue
        if abs(i - j) == 1:
            dp[i][j] = 1 if (nums[i] == nums[j]) else 0
        else:
            dp[i][j] = 1 if ((nums[i] == nums[j]) and (dp[i + 1][j - 1])) else 0

for s, e in questions:
    print(dp[s - 1][e - 1])