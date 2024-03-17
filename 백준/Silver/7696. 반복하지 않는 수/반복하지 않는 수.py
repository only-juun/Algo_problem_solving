def is_unique(num):
    digits = [False] * 10
    while num > 0:
        digit = num % 10
        if digits[digit]:
            return False
        digits[digit] = True
        num //= 10
    return True

arr = [0] * 1000001
count = 1
num = 1
while count <= 1000000:
    if is_unique(num):
        arr[count] = num
        count += 1
    num += 1

while True:
    n = int(input())
    if n == 0:
        break
    print(arr[n])
