from itertools import permutations

n = int(input())

arr = [''.join(map(str, perm)) for perm in permutations(range(1, 10), 3)]
ans = [''.join(map(str, perm)) for perm in permutations(range(1, 10), 3)]

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
    for a in arr:
        x, y = get_sb(a, str(num))
        if strike != x or ball != y:
            if a in ans:
                ans.remove(a)

print(len(ans))