from collections import deque
import sys

# 상수 정의
EMPTY, WALL, VIRUS = 0, 1, 2
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 입력 처리
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 초기화
area = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
min_virus_spread = sys.maxsize
empty_spaces, viruses, walls = [], [], 0

# 그리드 분석
for i in range(n):
    for j in range(m):
        if grid[i][j] == EMPTY:
            empty_spaces.append((i, j))
        elif grid[i][j] == VIRUS:
            viruses.append((i, j))
        else:
            walls += 1

def select_walls(cur, selected):
    global min_virus_spread
    if len(selected) == 3:
        min_virus_spread = min(calculate_safe_area(selected), min_virus_spread)
        return

    if cur >= len(empty_spaces):
        return 

    select_walls(cur + 1, selected + [empty_spaces[cur]])
    select_walls(cur + 1, selected)

def calculate_safe_area(walls):
    # 초기화
    for i in range(n):
        for j in range(m):
            area[i][j] = grid[i][j]
            visited[i][j] = False
    
    for x, y in walls:
        area[x][y] = WALL
    
    return spread_virus()

def spread_virus():
    q = deque(viruses)
    virus_count = 0

    while q:
        x, y = q.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            virus_count += 1
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and area[nx][ny] == EMPTY:
                    q.append((nx, ny))

    return virus_count

select_walls(0, [])

# 결과 출력
print((n * m) - min_virus_spread - walls - 3)
