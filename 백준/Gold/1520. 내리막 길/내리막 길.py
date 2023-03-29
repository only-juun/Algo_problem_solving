# boj 1520 내리막길
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

m, n = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(m)]

# dp[i][j] := (i, j)위치에 도달할 수 있는 경우의 수
dp = [[-1] * n for _ in range(m)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

def dfs(sx, sy):
    if (sx, sy) == (m - 1, n - 1):
        return 1

    if dp[sx][sy] != -1:
        return dp[sx][sy]
    
    cnt = 0
    for i in range(4):
        nx, ny = sx + dx[i], sy + dy[i]
        if in_range(nx, ny) and arr[sx][sy] > arr[nx][ny]:
            cnt += dfs(nx, ny)
    
    dp[sx][sy] = cnt
    return dp[sx][sy]

print(dfs(0,0))