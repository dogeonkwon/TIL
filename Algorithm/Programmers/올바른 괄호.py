def solution(s):
    answer = True
    res = []

    for i in s:
        if i == '(':
            res.append(i)
        else:
            if res:
                if res[-1] == '(':
                    res.pop()
            else:
                res.append(i)
    if res:
        answer = False
    return answer