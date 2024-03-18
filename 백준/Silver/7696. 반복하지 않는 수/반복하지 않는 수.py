while True:
    n = int(input())
    if n == 0:
        break
    n -= 1
    i = 1
    c = 9
    while True:
        if c > n:
            break
        n -= c
        c *= (10 - i)
        i += 1

    c = 1
    for j in range(i-1):
        c *= (9-j)
    l = []
    for j in range(i):
        l.append(n // c)
        n %= c
        c //= (9-j)
    l1 = [l[0] + 1]
    l2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    l2.remove(l[0]+1)
    for j in range(i-1):
        l1.append(l2.pop(l[j+1]))
    for x in l1:
        print(x, end="")
    print()
