def solution(msg):
    answer = []
    idx = {}

    for i in range(65, 91):
        idx[chr(i)] = i - 64

    n = len(msg)
    m = 0

    while m < n - 1:
        tmp = msg[m]
        s = m
        while m < n - 1:
            m += 1
            tmp += msg[m]
            if tmp not in idx:
                idx[tmp] = len(idx) + 1
                break

        answer.append(idx[msg[s:m]])

    answer.append(idx[msg[m]])

    return answer