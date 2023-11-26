n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

seq = set()

def choose(cur, arr):
    if cur == m:
        s = " ".join(map(str, arr))
        if s not in seq:
            seq.add(s)
            print(*arr, end ="\n")
        return

    for num in nums:
        if cur == 0 or num >= arr[cur - 1]:
            choose(cur + 1, arr + [num])

choose(0, [])
