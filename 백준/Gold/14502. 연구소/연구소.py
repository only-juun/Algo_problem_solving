from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
area = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = 0
zeros = []
virus = []
selected = []
walls = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            zeros.append((i, j))

        if grid[i][j] == 2:
            virus.append((i, j))
        
        if grid[i][j] == 1:
            walls += 1

def choose(cur):
    global ans
    if len(selected) == 3:
        ans = max(get_safe_area(), ans)
        return

    if cur >= len(zeros):
        return 
    
    selected.append(zeros[cur])
    choose(cur + 1)
    selected.pop()
    choose(cur + 1)

def get_safe_area():
    for i in range(n):
        for j in range(m):
            area[i][j] = grid[i][j]
            visited[i][j] = False
    
    for x, y in selected:
        area[x][y] = 1
    
    q = deque()
    cnt = 0
    for i, j in virus:
        q.append((i, j))
        visited[i][j] = True
        cnt += bfs(q)

    return (n * m) - cnt - walls - 3

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and area[x][y] == 0

def bfs(q):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    cnt = 1
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
         
    return cnt

choose(0)

print(ans)
