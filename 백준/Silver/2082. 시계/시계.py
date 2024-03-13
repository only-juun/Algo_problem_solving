number = {
    0: "####.##.##.####",
    1: "..#..#..#..#..#",
    2: "###..#####..###",
    3: "###..####..####",
    4: "#.##.####..#..#",
    5: "####..###..####",
    6: "####..####.####",
    7: "###..#..#..#..#",
    8: "####.#####.####",
    9: "####.####..####"
}

arr = [''.join(col) for col in zip(*(input().split() for _ in range(5)))]

def select_number(pos):
    # 자리에서 가능한 숫자들을 순차적으로 탐색
    for origin in range(digits[pos] + 1):
        # 현재 숫자(origin)가 조건을 만족하는지 검사
        for i in range(15):
            # 조건을 만족하지 않으면, 즉 number에서 꺼진 부분이 arr에 켜져 있으면
            if number[origin][i] == "." and arr[pos][i] == "#":
                # 이 숫자는 사용할 수 없으므로 다음 숫자로 넘어감
                break
        else:
            # 모든 검사를 통과했다면, 이 숫자는 사용 가능
            return str(origin)
        
answer = ""
digits = [2, 9, 5, 9]
for i in range(4):
    # 각 자리에서 가능한 작은 숫자를 선택
    answer += select_number(i)

print(f"{answer[:2]}:{answer[2:]}")