def solution(n, words):
    answer = [0, 0]
    num = 2
    idx = 1
    m = len(words)
    visited = [words[0]]

    while idx < m:
        if words[idx] in visited or words[idx - 1][-1] != words[idx][0]:
            answer = [num, idx // n + 1]
            break
        visited.append(words[idx])
        num %= n
        num += 1
        idx += 1

    return answer