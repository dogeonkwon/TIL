def solution(msg):
    answer = []
    idx = {}

    for i in range(65, 91):
        idx[chr(i)] = i - 64

    n = len(msg)
    m = 0
    tmp = msg[0]

    while m < n:
        if tmp in idx:
            m += 1
            if m < n:
                tmp += msg[m]
        else:
            idx[tmp] = len(idx) + 1
            answer.append(idx[tmp[0:len(tmp) - 1]])
            tmp = msg[m]

    answer.append(idx[tmp])

    return answer