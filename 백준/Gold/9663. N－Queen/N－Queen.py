n = int(input())
ans = 0
left_diagonal = [0] * (2 * n - 1)  # 주 대각선
right_diagonal = [0] * (2 * n - 1)  # 부 대각선
column = [0] * n  # 열

def solve(row):
    global ans
    if row == n:
        ans += 1
        return
    for col in range(n):
        if column[col] or left_diagonal[row + col] or right_diagonal[row - col + n - 1]:
            continue
        column[col] = left_diagonal[row + col] = right_diagonal[row - col + n - 1] = 1
        solve(row + 1)
        column[col] = left_diagonal[row + col] = right_diagonal[row - col + n - 1] = 0

solve(0)
print(ans)
