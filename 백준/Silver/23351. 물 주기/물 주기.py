n, k, a, b = map(int, input().split())

pots = [k for _ in range(n)]
ans = 1
while True:
    for i in range(n):
        if i < a:
            pots[i] += b
        pots[i] -= 1
        
    pots.sort()

    if pots[0] == 0:
        break
        
    ans += 1

print(ans)