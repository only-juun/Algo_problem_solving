from collections import deque

s = int(input())

q = deque()
q.append((1, 0))
# 현재 이모티콘의 개수와 클립보드 개수에 대해 2차원 배열로 저장
emoji = [[-1 for _ in range(1002)] for _ in range(1002)]
emoji[1][0] = 0

def in_range(x):
    return 0 <= x < 1002

while q:
    cur, clip = q.popleft()

    # 목표에 도달했을 경우 조기 종료
    if cur == s:
        break

    # 붙여넣기, 삭제하기에 대한 처리
    for nxt in (cur + clip, cur - 1):
        if in_range(nxt) and emoji[nxt][clip] == -1:
            q.append((nxt, clip))
            emoji[nxt][clip] = emoji[cur][clip] + 1
    
    # 클립보드에 복사하기 처리
    if emoji[cur][cur] == -1:
        q.append((cur, cur))
        emoji[cur][cur] = emoji[cur][clip] + 1

ans = -1
for i in range(1002):
    if emoji[s][i] != -1:
        if ans == -1 or emoji[s][i] < ans:
            ans = emoji[s][i]
print(ans)