import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    
    while(scoville[0] < K):
        if len(scoville) == 1:
            if scoville[0] < K:
                return -1

        first = hq.heappop(scoville)
        second = hq.heappop(scoville)
        hq.heappush(scoville, first+2*second)
        answer +=1
        
        
    return answer


def solution1(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer