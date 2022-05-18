def solution(numbers):
    zero_nine = [0,1,2,3,4,5,6,7,8,9]
    
    for num in numbers:
        zero_nine[num] = 0
    
    answer = sum(zero_nine)
    return answer