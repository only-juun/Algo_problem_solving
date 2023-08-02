# 입력
# 첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. 
# N은 2 이상 100 이하의 정수이다. 
# 둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 
# 각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. 높이는 1이상 100 이하의 정수이다.

# 출력
# 첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = []
min_height, max_height = sys.maxsize, -1
for _ in range(n):
    row = list(map(int, input().split()))
    min_height, max_height = min(min(row), min_height), max(max(row), max_height)
    arr.append(row)
visited = [[False for _ in range(n)] for _ in range(n)]

q = deque()

def initialize():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, height):
    return in_range(x, y) and arr[x][y] > height and not visited[x][y]

def bfs(height):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, height):
                visited[nx][ny] = True
                q.append((nx, ny))

answer = 1

for height in range(min_height, max_height):
    cnt = 0
    for i in range(n):
        for j in range(n):   
            if arr[i][j] > height and not visited[i][j]:
                visited[i][j] = True
                q.append((i, j))
                bfs(height)
                cnt += 1
    initialize()
    answer = max(cnt, answer)

print(answer)