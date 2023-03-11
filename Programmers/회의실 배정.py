# 입력
# 회의의 수 N(1 ≤ N ≤ 100,000)
# 둘째 줄부터 N+1 줄까지 각 회의의 정보
# 공백을 사이에 두고 회의의 시작시간과 끝나는 시간
# 시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0
n = int(input())
meetings = [list(map(int,input().split())) for _ in range(n)]

meetings.sort(key=lambda x: x[0]) # 시작 시간 기준으로 정렬
meetings.sort(key=lambda x: x[1]) # 종료 시간 기준으로 정렬

ans = 0
end = 0
for a in meetings:
    if a[0] >= end:
        ans += 1
        end = a[1]
        
# 출력: 최대 사용할 수 있는 회의의 최대 개수
print(ans)