from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    answer = 0

    cache = deque()

    for i in cities:
        s = i.lower()
        if s not in cache:
            answer += 5
            if len(cache) == cacheSize:
                cache.popleft()
                cache.append(s)
            else:
                cache.append(s)
        else:
            answer += 1
            cache.remove(s)
            cache.append(s)

    return answer