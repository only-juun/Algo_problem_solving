# boj 11728.배열 합치기

# 입력
n, m = tuple(map(int, input().split())) # n: a 배열의 크기, m: b 배열의 크기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

arr = []
for i in a:
    arr.append(i)
for i in b:
    arr.append(i)

arr.sort()
print(*arr)