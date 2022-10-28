def solution(n):
    answer = 0
    s = bin(n)[2::]
    k = s.count('1')
    tmp = n + 1

    while True:
        sub = bin(tmp)[2::]

        if k == sub.count('1'):
            answer = int(sub, 2)
            break
        tmp += 1

    return answer