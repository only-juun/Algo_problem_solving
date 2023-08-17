import sys

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start, end = 0, n - 1
cnt = sys.maxsize
answer = [0, 0]

while start != end:
    left, right = arr[start], arr[end]

    x = left + right
    if abs(x) <= cnt:
        cnt = min(abs(x), cnt)
        answer = [left, right]
    
    if x < 0:
        start += 1
    else:
        end -= 1
    
print(*answer)
