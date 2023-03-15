from collections import deque
import sys
INF = sys.maxsize

n, k = tuple(map(int, input().split()))
dist = [INF] * 100001
dist[n] = 0
q = deque()
q.append(n)

def mul_2(x):
    while True:
        if (2 * x) >= 100001 or dist[2 * x] != INF:
            break
        dist[2 * x] = dist[x]
        q.append(2 * x)
        x *= 2

def bfs():
    while q:
        x = q.popleft()
        mul_2(x)

        if x == k:
            return dist[x]
        
        for nx in [x - 1, x + 1]:
            if 0 <= nx < 100001 and dist[nx] == INF:
                dist[nx] = dist[x] + 1
                q.append(nx)
                
print(bfs())