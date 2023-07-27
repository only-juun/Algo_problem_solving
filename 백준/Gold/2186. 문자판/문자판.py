import sys
input = sys.stdin.readline

# 입력받기
n, m, k = list(map(int, input().strip().split()))
board = [list(input().strip()) for _ in range(n)]
word = input().strip()

dxs = [-1,0,1,0]
dys = [0,1,0,-1]
dp = [[[-1] * len(word) for i in range(m)] for i in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, cur):
    return in_range(x, y) and board[x][y] == word[cur]
            
def dfs(x, y, cur):
    global answer

    # 이미 방문한 곳인 경우
    if dp[x][y][cur] != -1:
        return dp[x][y][cur]
    
    # 단어를 완성한 경우
    if cur == len(word) - 1:
        return 1
    
    # 필요한 문자가 아닌 경우
    if board[x][y] != word[cur]:
        return 0
	
    # 상하좌우 k거리 떨어진 곳 전부 탐색
    cnt = 0
    for i in range(1, k + 1):
        for dx, dy in zip(dxs, dys):
            nx = x + i * dx
            ny = y + i * dy
            if can_go(nx, ny, cur + 1):
                cnt += dfs(nx, ny, cur + 1)
    dp[x][y][cur] = cnt

    return dp[x][y][cur]

answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == word[0]:
            answer += dfs(i, j, 0)

print(answer)