def solution(progresses, speeds):
    answer = []
    n = len(progresses)

    if n == 0:
        return answer
    else:
        if (100 - progresses[0]) % speeds[0]:
            s = ((100 - progresses[0]) // speeds[0]) + 1
        else:
            s = (100 - progresses[0]) // speeds[0]
        answer.append(1)
        for i in range(1, n):
            if (100 - progresses[i]) % speeds[i]:
                k = ((100 - progresses[i]) // speeds[i]) + 1
            else:
                k = (100 - progresses[i]) // speeds[i]
            if k > s:
                answer.append(1)
                s = k
            else:
                answer[-1] += 1

        return answer