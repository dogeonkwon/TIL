def solution(s):
    answer = 1

    res = []

    for i in s:
        if len(res) > 0 and res[-1] == i:
            res.pop()
        else:
            res.append(i)

    if res:
        answer = 0

    return answer