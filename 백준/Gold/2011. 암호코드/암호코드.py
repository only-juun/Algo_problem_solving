# boj 2011. 암호코드
import sys

MOD = 1000000
n = input()

def a_to_i(num):
    return 1 <= int(num) <= 9

def j_to_z(num):
    return 10 <= int(num) <= 26

dp = [0] * 5000
dp[0] = 1 if a_to_i(n[0]) else 0
if len(n) == 1:
    print(dp[len(n) - 1])
    sys.exit()
dp[1] = dp[0] if a_to_i(n[1]) else 0
if j_to_z(n[:2]):
    dp[1] += 1

for i in range(2, len(n)):
    if a_to_i(n[i]):
        dp[i] += dp[i - 1]
    if j_to_z(n[i - 1: i + 1]):
        dp[i] += dp[i - 2]
    dp[i] %= MOD

print(dp[len(n) - 1])