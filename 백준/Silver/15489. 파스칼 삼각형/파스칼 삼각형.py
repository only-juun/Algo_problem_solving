# 15489. 파스칼 삼각형

# 입력 받기
# r번째 줄, c번째 수를 위 꼭짓점, 한 변의 길이 w
r, c, w = map(int, input().split())

pt = [[0] * (r + w + 1) for _ in range(r + w + 1)]

# 파스칼 삼각형 만들기
for i in range(r + w):
    for j in range(i + 1):
        if j == 0 or j == (i + 1):
            pt[i][j] = 1
        else:
            pt[i][j] = pt[i - 1][j - 1] + pt[i - 1][j]

ans = 0
for i in range(w):
    for j in range(i + 1):
        ans += pt[r + i - 1][c + j - 1]

print(ans)