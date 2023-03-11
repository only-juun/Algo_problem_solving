# 줄을 서 있는 사람의 수 N
# 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때,
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램

# 입력: 사람의 수 N(1 ≤ N ≤ 1,000)
n = int(input())
# 입력: 각 사람이 돈을 인출하는데 걸리는 시간 Pi(1 ≤ Pi ≤ 1,000)
wd_time = list(map(int, input().split()))

# 인출에 걸리는 시간이 적은 사람부터 줄을 서는 것이 유리
wd_time.sort()

answer = 0
for i in range(n):
	answer += (n - i) * wd_time[i]

print(answer)