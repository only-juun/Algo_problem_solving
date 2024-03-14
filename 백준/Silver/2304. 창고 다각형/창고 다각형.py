n = int(input())
s = list()
for _ in range(n):
    l, h = map(int, input().split())
    s.append((l, h))

s.sort(key = lambda x: x[0])

answer = 0
s_width, s_height = s[0][0], s[0][1]
for l, h in s[1:]:
    if h > s_height:
        answer += s_height * abs(l - s_width)
        s_width, s_height = l, h

l_width, l_height = s[-1][0], s[-1][1]
for l, h in s[-1::-1]:
    if h > l_height:
        answer += l_height * abs(l - l_width)
        l_width, l_height = l, h

print(answer + (s_height * (abs(s_width - l_width) + 1)))