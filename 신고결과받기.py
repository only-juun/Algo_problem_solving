def solution1(id_list, report, k):
    ids=len(id_list)
    
    hello = [[0 for j in range(ids)] for i in range(ids)]
    limit=[0 for i in range(ids)]
    answer=[0 for i in range(ids)]
    
    report = set(report)
    report = list(report)
    
    for i in range(len(report)):
        reporter, reportee = report[i].split(" ")
        hello[id_list.index(reporter)][id_list.index(reportee)] = 1
    
    for i in range(ids):
        for j in range(ids):
            limit[j] += hello[i][j]
            
    
    for i in range(ids):
        if limit[i] >= k:
            for j in range(ids):
                if hello[j][i] == 1:
                    answer[j] += 1

    return answer




def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    # 신고 당한 사람 카운트
    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        # 신고 당한 횟수가 k를 넘을 경우
        if reports[r.split()[1]] >= k:
            #신고한 사람의 메일 횟수 +1
            answer[id_list.index(r.split()[0])] += 1

    return answer