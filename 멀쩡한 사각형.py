from math import gcd

def solution(w,h):
    whole = w*h
    broken = w+h-gcd(w,h)
    
    return whole-broken

def solution1(w,h):
    answer = 0

    if w == h:# /wo: timeout at tc11
        return sum(range(1,w))*2

    for i in range(1, w):
        answer += (h*i)//w
    return answer*2