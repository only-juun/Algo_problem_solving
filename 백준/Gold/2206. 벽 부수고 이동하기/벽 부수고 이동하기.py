from collections import deque
import sys
INF = sys.maxsize
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs():
    q = deque()
    q.append((0, 0, 1))
    visited[0][0][1] = 1

    while q:
        x, y, wall = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][wall]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == '1' and wall == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append((nx, ny, 0))

                elif board[nx][ny] == '0' and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx, ny, wall))

    return -1

print(bfs())
