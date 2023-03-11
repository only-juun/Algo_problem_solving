def solution(nums):
    answer = 0
    n = len(nums)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                p = nums[i] + nums[j] + nums[k]
                if is_prime(p):
                    answer += 1
    return answer

def is_prime(a):
    if a < 2:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True