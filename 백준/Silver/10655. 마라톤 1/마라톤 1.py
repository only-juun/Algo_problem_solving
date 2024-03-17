import sys

def get_dist(idx):
    cnt = forward[idx - 1] + backward[idx + 1]
    x = abs(check_points[idx - 1][0] - check_points[idx + 1][0])
    y = abs(check_points[idx - 1][1] - check_points[idx + 1][1])
    return cnt + x + y


n = int(input()) 
check_points = []

for _ in range(n):
    x = tuple(map(int, input().split()))
    check_points.append(x)

forward = [0] * (n)
for i in range(1, n):
    x = abs(check_points[i][0] - check_points[i - 1][0])
    y = abs(check_points[i][1] - check_points[i - 1][1])
    forward[i] = forward[i - 1] + (x + y)

backward = [0] * (n)
for i in range(n - 2, -1, -1):
    x = abs(check_points[i + 1][0] - check_points[i][0])
    y = abs(check_points[i + 1][1] - check_points[i][1])
    backward[i] = backward[i + 1] + (x + y)

ans = sys.maxsize
for i in range(1, n - 1):
    ans = min(ans, get_dist(i))

print(ans)