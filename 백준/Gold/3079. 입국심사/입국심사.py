# boj 3079.입국심사
import sys
input = sys.stdin.readline
INF = sys.maxsize

# 입력받기
n, m = tuple(map(int, input().split()))
t = [int(input()) for _ in range(n)]
t.sort(reverse=True)

# 소요 시간에 대해 끝내는 것이 가능한지 확인
def is_possible(target):
    cnt = 0
    for x in t:
        cnt += (target//x)
        if cnt >= m:
            return True

    return False

left = 0
right = m * t[-1]
answer = INF
# 소요시간에 대해 이분 탐색
while left <= right:
    mid = (left + right) // 2

    # 해당 소요시간에 끝내는 것이 
    # 가능한 경우
    if is_possible(mid):
        # 가능한 시간 갱신
        answer = mid
        # 더 작은 값에 대해서 탐색
        right = mid - 1
    # 불가능한 경우
    else:
        # 더 큰 값에 대해서 탐색
        left = mid + 1

print(answer)