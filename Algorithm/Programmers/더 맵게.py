def solution(scoville, K):
    answer = 0
    scoville.sort(reverse=True)
    n = len(scoville)

    while scoville:
        if scoville[-1] >= K:
            break
        answer += 1
        tmp = scoville.pop() + scoville.pop() * 2
        scoville.append(tmp)
        scoville.sort(reverse=True)

    return answer