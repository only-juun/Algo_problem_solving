def is_unique(num):
    bit_mask = 0
    while num > 0:
        digit = num % 10
        if bit_mask & (1 << digit):
            return False
        bit_mask |= (1 << digit)
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
