from collections import deque


def solution(s):
    answer = 0

    arr = deque(s)
    n = len(s)
    visited = []

    for i in range(n):
        stop = 0
        for j in range(n):
            if stop:
                break
            elif arr[j] in ['(', '{', '[']:
                visited.append(arr[j])
            elif visited == []:
                stop = 1
            else:
                if arr[j] == ')':
                    if visited[-1] == '(':
                        visited.pop()
                    else:
                        stop = 1
                elif arr[j] == '}':
                    if visited[-1] == '{':
                        visited.pop()
                    else:
                        stop = 1
                elif arr[j] == ']':
                    if visited[-1] == '[':
                        visited.pop()
                    else:
                        stop = 1

        if not stop and visited == []:
            answer += 1
        v = arr.popleft()
        arr.append(v)

    return answer