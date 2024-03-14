n, k, a, b = map(int, input().split())
# n개 화분, 각 화분의 수분k, 연속된 a개 화분에 물주면 b수분 증가
# 모든 화분이 1씩 감소
# 수분 0은 다이

pots = [k for _ in range(n)]
ans = 1
while True:
    # 연속 a개 화분에 물주기
    for i in range(n):
        if pots[i] == min(pots):
            for j in range(a):
                pots[i + j] += b
            break

    # 모든 수분 1 감소
    for i in range(n):
        pots[i] -= 1

    if min(pots) == 0:
        break

    ans += 1

print(ans)