import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2:
        if scoville[0] >= K:
            break
        answer += 1
        tmp = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, tmp)

    if scoville[0] < K:
        answer = -1

    return answer