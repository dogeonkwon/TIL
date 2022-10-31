def solution(brown, yellow):
    answer = []

    for i in range(1, brown // 2):
        j = brown // 2 - i
        if yellow == i * j - 2 * j and i >= j + 2:
            answer = [i, j + 2]
            break

    return answer