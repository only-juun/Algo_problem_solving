import math as m
def solution(progresses, speeds):
    answer = []
    required = []
    for i,j in zip(progresses, speeds):
        required.append(m.ceil((100-i)/j))
    
    i = 0
    for j in range(1,len(required)):
        if required[i] < required[j]:
            answer.append(j-i)
            i = j
        if j == len(required)-1:
            answer.append(j-i+1)
        
    return answer

def solution1(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]