import sys

n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

left, right = max(arr), sum(arr)
ans = right

def is_possible(target):
    cnt = 1
    s = 0
    for i in range(n):
        if (s + arr[i]) <= target:
            s += arr[i]
        else:
            s = arr[i]
            cnt += 1
            if cnt > m:
                return False  
    return True

while left <= right:
    mid = (left + right) // 2

    if is_possible(mid):
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1
print(ans)