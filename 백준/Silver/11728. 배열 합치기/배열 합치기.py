# boj 11728.배열 합치기

# 입력
n, m = tuple(map(int, input().split())) # n: a 배열의 크기, m: b 배열의 크기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
a.append(10**9 + 1)
b.append(10**9 + 1)

a_pointer = 0
b_pointer = 0

while a_pointer < n or b_pointer < m:
    if a[a_pointer] <= b[b_pointer]:
        print(a[a_pointer], end = ' ')
        a_pointer += 1
    else:
        print(b[b_pointer], end = ' ')
        b_pointer += 1