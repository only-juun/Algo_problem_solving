# boj 2003. 수들의 합2

# 입력 받기
n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

# sum(nums[i]~nums[j]) = m인 경우의 수
# 투포인터 사용
r = 0
cnt = 0
ans = 0
# left pointer를 하나씩 확인하면서
for l in range(n):
    # right pointer를 이동시키면서
    # n보다는 작고, 합이 m보다는 작은 동안
    # 합을 구해주기
    # cnt >= m 이면 종료
    while r < n and cnt < m:
        cnt += nums[r]
        r += 1
    
    # 합이 m이라면 경우의 수 증가
    if cnt == m:
        ans += 1
    
    # left pointer를 이동시킬 것이므로
    # left 위치의 값을 빼주기
    cnt -= nums[l]

print(ans)