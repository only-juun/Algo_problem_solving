import sys
import heapq
INF = sys.maxsize

m, n = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]
result = [[INF]*m for _ in range(n)]

hq = []
heapq.heappush(hq, (0, 0, 0))
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and result[x][y] == INF

while hq:
    r, x, y = heapq.heappop(hq)
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        nr = r
        if can_go(nx, ny):
            if miro[nx][ny] == 1:
                nr = r + 1
            if r < result[nx][ny] and result[nx][ny] >= nr:
                result[nx][ny] = nr
                heapq.heappush(hq, (nr, nx, ny))

ans = result[n-1][m-1]
print(ans if ans != INF else 0)