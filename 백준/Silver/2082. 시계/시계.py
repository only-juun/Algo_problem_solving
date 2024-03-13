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

arr = ['' for _ in range(4)]
for _ in range(5):
    line = list(input().split())
    for i in range(4):
        arr[i] += line[i]

# 켜지지 않아야 하는 것이 켜진 경우는 없다 
# 정상 숫자에서 꺼진 부분에 불이 있는 것은 배제
# 첫번째 자리: 0,1,2 중에서 가능한 숫자 먼저 선택
# 두번째 자리: 0-9 중에서 가능한 숫자 먼저 선택
# 세번째 자리: 0-5 중에서 가능한 숫자 먼저 선택
# 네번째 자리: 0-9 중에서 가능한 숫자 먼저 선택
def select_number(pos):
    # 자리에서 가능한 숫자들을 순차적으로 탐색
    for origin in range(digits[pos] + 1):
        flag = True
        # 비교하면서 origin에서 꺼진 부분이 arr에 켜져있으면 다음 숫자
        # 아니라면 숫자를 고르고 return
        for i in range(15):
            if number[origin][i] == "." and arr[pos][i] == "#":
                flag = False
                break
        if flag:
            return str(origin)
        

answer = ""
digits = [2, 9, 5, 9]
for i in range(4):
    # 각 자리에서 가능한 작은 숫자를 선택
    answer += select_number(i)

print(answer[:2] + ":" + answer[2:])