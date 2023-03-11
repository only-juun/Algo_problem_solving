def solution(answers):
    answer = []
    person1 = [1, 2, 3, 4, 5]*2000
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]*1250
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000
    
    a = grading(person1[:len(answers)],answers)
    b = grading(person2[:len(answers)],answers)
    c = grading(person3[:len(answers)],answers)
    
    score = [a,b,c]
    
    for idx, s in enumerate(score):
        if s == max(score):
            answer.append(idx+1)
            
    return answer
        
def grading(person, answers):
    score = 0
    for i,j in zip(person,answers):
        if i==j:
            score +=1
            
    return score


def solution1(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result