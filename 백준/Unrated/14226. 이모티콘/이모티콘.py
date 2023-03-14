from collections import deque

s = int(input())

q = deque()
q.append((1, 0))
emoji = [[-1 for _ in range(1002)] for _ in range(1002)]
emoji[1][0] = 0

def in_range(x):
    return 0 <= x < 1002

while q:
    cur, clip = q.popleft()

    if cur == s:
        break

    if in_range(cur + clip) and emoji[cur + clip][clip] == -1:
        q.append((cur + clip, clip))
        emoji[cur + clip][clip] = emoji[cur][clip] + 1
    
    if in_range(cur - 1) and emoji[cur - 1][clip] == -1:
        q.append((cur - 1, clip))
        emoji[cur - 1][clip] = emoji[cur][clip] + 1
    
    if emoji[cur][cur] == -1:
        q.append((cur, cur))
        emoji[cur][cur] = emoji[cur][clip] + 1

ans = -1
for i in range(1002):
    if emoji[s][i] != -1:
        if ans == -1 or emoji[s][i] < ans:
            ans = emoji[s][i]
print(ans)