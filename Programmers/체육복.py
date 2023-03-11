def in_range(n, i):
    return 0 <= i < n

def solution(n, lost, reserve):
    # 초기 학생 배열(전부 체육복 소지)
    ans = [1 for _ in range(n)]
    
    lost.sort()
    reserve.sort()
    
    # 잃어버린 학생들
    for i in lost:
        ans[i - 1] -= 1
    
    # 여벌 옷이 있는 학생들
    for i in reserve:
        ans[i - 1] += 1
    
    # 여벌 옷이 있는 학생들 중 도난당하지 않은 학생들에 대해
    for j in reserve:
        if ans[j - 1] == 2:
            # 앞 번호가 체육복이 없을 경우
            if in_range(n, j - 2) and ans[j - 2] == 0:
                ans[j - 1] -= 1
                ans[j - 2] += 1
            # 뒷 번호가 체육복이 없을 경우
            elif in_range(n, j) and ans[j] == 0:
                ans[j - 1] -= 1
                ans[j] += 1
                
    answer = 0
    
    # 수업을 들을 수 있는 학생 수
    for i in ans:
        if i > 0:
            answer += 1
    
    return answer