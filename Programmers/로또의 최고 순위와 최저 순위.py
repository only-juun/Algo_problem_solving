def solution(lottos, win_nums):
    lottos = sorted(lottos)
    win_nums = sorted(win_nums)
    
    zeros = 0
    cnt = 0
    grade = 7
    
    for i in range(6):
        if lottos[i] == 0:
            zeros += 1
            continue
        for j in range(6):
            if lottos[i] == win_nums[j]:
                cnt += 1
                continue
    
    if zeros == 0:
        if cnt == 0:
            high = grade - 1
            low = grade - 1
        else:
            high = grade - cnt
            low = grade - cnt
    else:
        if cnt == 0:
            high = grade - zeros
            low = grade - 1
        else:
            high = grade - zeros - cnt
            low = grade - cnt
        
        
    answer = [high, low]
    return answer