def solution(n):
    answer = 0
    for i in range(1, n + 1):
        tmp = i
        add = i + 1

        while tmp <= n:
            if tmp == n:
                answer += 1
                break
            tmp += add
            add += 1

    return answer