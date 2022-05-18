def solution(numbers, hand):
    left = [1,4,7]
    right = [3,6,9]
    l_now = '*'
    r_now = '#'
    answer = ''
    # 키패드 매핑
    keypad = {1:[0,0],2:[0,1],3:[0,2],
              4:[1,0],5:[1,1],6:[1,2],
              7:[2,0],8:[2,1],9:[2,2],
              '*':[3,0],0:[3,1],'#':[3,2]}
    
    for num in numbers:
        if num in left:
            l_now = num
            answer += 'L'
        elif num in right:
            r_now = num
            answer += 'R'
        else:
            if abs(keypad[l_now][0] - keypad[num][0])+abs(keypad[l_now][1]-keypad[num][1]) < \
                abs(keypad[r_now][0] - keypad[num][0])+abs(keypad[r_now][1]-keypad[num][1]):
                l_now = num
                answer += 'L'
            elif abs(keypad[l_now][0] - keypad[num][0])+abs(keypad[l_now][1]-keypad[num][1]) > \
                abs(keypad[r_now][0] - keypad[num][0])+abs(keypad[r_now][1]-keypad[num][1]):
                r_now = num
                answer += 'R'
            else:
                if hand == 'right':
                    r_now = num
                    answer += 'R'
                else:
                    l_now = num
                    answer += 'L'
                
    return answer