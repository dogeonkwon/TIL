from itertools import combinations


def solution(clothes):
    answer = 0
    n = len(clothes)
    dressroom = {}
    keys = []
    for i in range(n):
        if dressroom.get(clothes[i][1]) == None:
            dressroom[clothes[i][1]] = [clothes[i][0]]
            keys.append(clothes[i][1])
        else:
            dressroom[clothes[i][1]].append(clothes[i][0])

    m = len(dressroom)
    if m >= 2:
        tmp = 1
        for j in range(m):
            k = len(dressroom[keys[j]])
            tmp *= k + 1
        answer += tmp - 1
    else:
        answer += len(dressroom[keys[0]])

    return answer