import sys
from itertools import permutations as p
input = sys.stdin.readline

n = int(input())

arr = list(p('123456789', 3))

def get_sb(a, num):
    s, b = 0, 0
    for x, y in zip(list(a), list(num)):
        if x == y:
            s += 1
        elif x in list(num):
            b += 1
    return (s, b)


for i in range(n):
    num, strike, ball = map(int, input().split())
    temp = []
    for a in arr:
        x, y = get_sb(a, str(num))
        if strike == x and ball == y:
            temp.append(a)

    arr = temp

print(len(arr))