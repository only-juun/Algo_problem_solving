# boj 7576.토마토
import sys
from collections import deque
input = sys.stdin.readline

# 입력받기
m, n = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [1,0,-1,0], [0,1,0,-1]

answer = 0
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j, 0))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and arr[x][y] == 0

def bfs():
    global answer
    while q:
        x, y, cnt = q.popleft()
        
        answer = max(answer, cnt)

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                arr[nx][ny] = 1
                q.append((nx, ny, cnt + 1))

bfs()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            answer = -1

print(answer)

