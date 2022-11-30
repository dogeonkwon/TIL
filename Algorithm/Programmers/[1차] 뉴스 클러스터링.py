import math


def solution(str1, str2):
    answer = 0
    intersection = 0  # 교집합
    union = 0  # 합집합
    arr1 = []
    n = len(str1)
    m = len(str2)

    for i in range(n - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            dict1.append(str1[i:i + 2].upper())
            union += 1

    for j in range(m - 1):
        if str2[j].isalpha() and str2[j + 1].isalpha():
            union += 1
            if str2[j:j + 2].upper() in dict1:
                intersection += 1
                dict1.remove(str2[j:j + 2].upper())

    union -= intersection
    if union == 0:
        answer = 65536
    else:
        answer = (intersection / union) * 65536
        answer = math.trunc(answer)

    return answer