# boj 21921.블로그

# 입력 받기
n, x = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

left = 0
right = x
m = sum(nums[left:right])
ans = 1
cnt = m
while right < n:
    cnt = cnt - nums[left] + nums[right]
    
    if cnt == m:
        ans += 1
    elif cnt > m:
        ans = 1
        m = cnt
    right += 1
    left += 1


if m == 0:
    print('SAD')
else:
    print(m, ans, sep='\n')