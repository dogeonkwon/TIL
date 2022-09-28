import sys, collections

def BFS(start, visited):

    q = collections.deque([[start, 1]])
    stop = 1
    visited[start] = True

    while q:
        if not stop:
            break
        v = q.popleft()
        for i in (v[0]+1, v[0]-1, v[0]*2):
            if i == k:
                stop = 0
                print(v[1])
                break
            elif not visited[i]:
                visited[i] = True
                q.append([i, v[1]+1])


n, k = map(int, sys.stdin.readline().split())
visit = [False] * 100001
if n == k:
    print(0)
else:
    BFS(n, visit)