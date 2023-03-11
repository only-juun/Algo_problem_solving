def solution1(n):
    answer = ''
    base = ['1','2','4']
    while(n > 3):
        if n%3 == 0:
            answer = base[2] + answer
            n = n//3 - 1
        else:
            answer = str(n%3) + answer
            n = n//3
    answer = base[n-1] + answer
    
    return answer

def solution(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer