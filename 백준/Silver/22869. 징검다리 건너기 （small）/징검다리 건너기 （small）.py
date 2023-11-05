n, k = map(int, input().split())
arr = list(map(int, input().split()))

visited = [False] * n
visited[0] = True

for start in range(n - 1):
    for end in range(start + 1, n):
        if visited[start] and (end - start) * (1 + abs(arr[start] - arr[end])) <= k:
            visited[end] = True

print("YES" if visited[n - 1] else "NO")