from collections import deque

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m
    
    def can_go(x, y):
        return in_range(x, y) and not visited[x][y] and maps[x][y] != 'X'
    
    def bfs():
        dxs, dys = [-1, 1, 0, 0],  [0, 0, -1, 1]
        cnt = 0
        while q:
            x, y = q.pop()
            cnt += int(maps[x][y])
            
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if can_go(nx, ny):
                    visited[nx][ny] = True
                    q.append((nx, ny))
        return cnt
    
    q = deque()
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited[i][j] = True
                q.append((i,j))
                cnt = bfs()
                answer.append(cnt)
                
    answer.sort()
    
    return [-1] if not answer else answer