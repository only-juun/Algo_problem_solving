from collections import deque

# n, k 입력받기
n, k = tuple(map(int, input().split()))

def path(a):
    arr = [a]
    while a != n:
        arr.append(route[a])
        a = route[a]
    return arr[::-1]

def bfs():
    while q:
        x = q.popleft()

        if x == k:
            return
        
        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx < 100001 and not dist[nx]:
                dist[nx] = dist[x] + 1
                route[nx] = x
                q.append(nx)

dist = [0] * 100001
route = [0] * 100001
q = deque()
q.append(n)
bfs()

print(dist[k])
print(*path(k))