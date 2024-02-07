import sys

input = sys.stdin.readline

T = int(input())

def get_answer(a, b):
    c = a % 10
    for i in range(1, b):
        c = (c * a) % 10

    return c if c != 0 else 10

for _ in range(T):
    a, b = map(int, input().split())
    print(get_answer(a, b))