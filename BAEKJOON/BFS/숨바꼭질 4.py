import sys, collections

n, k = map(int, sys.stdin.readline().split())

visited = [0] * 100001

q = collections.deque([[n, [n]]])
visited[n] = 1

while q:
    v = q.popleft()

    if v[0] == k:
        print(visited[v[0]] - 1)
        print(*v[1])
        break

    tmp = v[1]
    for i in (v[0] - 1, v[0]+1, v[0]*2):
        if not visited[i] and 0 <= i <= 100000:
            sub = v[1] + [i]
            q.append([i, sub])
            visited[i] = visited[v[0]] + 1