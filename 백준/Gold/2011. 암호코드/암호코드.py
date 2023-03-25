import sys

MOD = 1000000

password = [0] + list(map(int, input()))
dp = [0] * len(password)
dp[0] = 1
dp[1] = 1 if password[1] != 0 else 0

if not dp[1]:
    print(0)
    sys.exit()

def j_to_z(num):
    return 10 <= num <= 26

for i in range(2, len(password)):
    if password[i] != 0:
        dp[i] += dp[i - 1]

    num = password[i-1] * 10 + password[i]
    if j_to_z(num):
        dp[i] += dp[i - 2]
    dp[i] %= MOD

print(dp[len(password) - 1])
