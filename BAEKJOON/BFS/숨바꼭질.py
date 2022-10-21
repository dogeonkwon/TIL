import sys, collections

n, k = map(int, sys.stdin.readline().split())

q = collections.deque([n])

visited = [0] * 100001
visited[n] = 1

while q:
    v = q.popleft()

    if v == k:
        break

    for i in (v+1, v-1, v*2):
        if 0 <= i <= 100000 and not visited[i]:
            visited[i] = visited[v] + 1
            q.append(i)

print(visited[k]-1)