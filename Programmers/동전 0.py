
# 동전은 총 N종류
# 동전을 적절히 사용해서 그 가치의 합을 K
# 이때 필요한 동전 개수의 최솟값
# 입력: N과 K(1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
n, k = tuple(map(int, input().split()))

# N개의 줄에 동전의 가치 Ai가 오름차순
# (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
value = [0]
for _ in range(n):
	value.append(int(input()))

value.sort(reverse = True)
answer = 0
for i in value:
	if k == 0:
		break
	if i > k:
		continue
	else:
		answer += k//i
		k %= i

print(answer)