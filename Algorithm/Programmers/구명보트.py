from collections import deque


def solution(people, limit):
    answer = 0

    n = len(people)
    people.sort(reverse=True)

    m = 0
    q = deque(people)

    while q:
        v = q.popleft()
        s = limit - v
        while s >= people[n - 1 - m] and q:
            s -= people[n - 1 - m]
            q.pop()
            m += 1

        answer += 1
    return answer