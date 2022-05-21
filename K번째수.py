def solution(array, commands):
    answer = []
    for cmd in commands:
        i,j,k = cmd
        answer.append(sorted(array[i-1:j])[k-1])
        
    return answer

def solution1(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

