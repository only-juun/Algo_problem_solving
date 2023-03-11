import sys
def solution(n, times):
    answer = 0
    left = 0
    right = sys.maxsize
    
    def is_possible(target):
        cnt = 0
        for time in times:
            cnt += (target // time)
        return cnt >= n
    
    while left <= right:
        mid = (left + right) // 2
        
        if is_possible(mid):
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    
    return answer