def solution(board, moves):
    answer = 0
    now = 0
    basket = [0]*len(moves)
    
    for move in moves:
        for x in board:
            if x[move-1] != 0:
                basket[now] = x[move-1]
                x[move-1] = 0
                if now != 0 and basket[now] == basket[now-1]:
                    now -= 1
                    answer += 2
                else:
                    now += 1
                break
                    
    return answer