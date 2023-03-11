t = int(input())
def gcd(nums):
    x, y = nums
    while y:
        x, y = y, x % y
    return x

def choose(cur, cnt, n):
    global ans
    if cnt == 2:
        ans = max(ans, gcd(nums))
        return
    
    if cur == n:
        return
    
    selected[cur] = True
    nums.append(arr[cur])
    choose(cur + 1, cnt + 1, n)
    selected[cur] = False
    nums.pop()
    choose(cur + 1, cnt, n)
    
ans = 0
selected = []
arr = []
nums = []
for _ in range(t):
    arr = list(map(int, input().split()))
    n = len(arr)
    ans = 0
    selected = [False for _ in range(n)]
    choose(0, 0, n)
    print(ans)
