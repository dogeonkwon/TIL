def solution(n, left, right):
    answer = []
    k = 1

    for i in range(n):
        for j in range(n):
            if left <= (i * n) + j <= right:
                if j + 1 <= k:
                    answer.append(k)
                else:
                    answer.append(j + 1)
        k += 1

    return answer