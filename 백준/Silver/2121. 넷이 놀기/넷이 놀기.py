import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

pos = set()
for _ in range(n):
    x, y = map(int, input().split())
    pos.add((x, y))

def is_possible(x, y):
    if (x + a, y + b) in pos and (x + a, y) in pos and (x, y + b) in pos:
        return True
    return False

ans = 0
for x, y in pos:
    if is_possible(x, y):
        ans += 1

print(ans)

